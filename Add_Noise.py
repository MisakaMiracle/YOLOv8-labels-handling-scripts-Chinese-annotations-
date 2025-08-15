import cv2
import numpy as np
import os
import shutil
####重要!!!
####重要!!!
####重要!!!
####此版本禁止中文路径、文件名。输入图像为'.jpg','.png', '.jpeg'，输出统一为'.jpg'。
#This version prohibits Chinese paths and file names. Input images must be in .jpg, .png, or .jpeg format, and output will be in .jpg format.
####重要!!!
####重要!!!
####重要!!!

# 高斯噪声
def add_gaussian_noise(image, mean=0, std=5):
    noise = np.random.normal(mean, std, image.shape).astype(np.int16)
    noisy = image.astype(np.int16) + noise
    return np.clip(noisy, 0, 255).astype(np.uint8)

# 椒盐噪声
def add_salt_pepper_noise(image, amount=0.005, salt_vs_pepper=0.5):
    noisy = image.copy()
    h, w, _ = noisy.shape
    num_noise = int(amount * h * w)

    # 添加盐（白点）
    for _ in range(int(num_noise * salt_vs_pepper)):
        x = np.random.randint(0, w)
        y = np.random.randint(0, h)
        noisy[y, x] = [255, 255, 255]

    # 添加胡椒（黑点）
    for _ in range(int(num_noise * (1 - salt_vs_pepper))):
        x = np.random.randint(0, w)
        y = np.random.randint(0, h)
        noisy[y, x] = [0, 0, 0]

    return noisy

# 泊松噪声
def add_poisson_noise(image):
    vals = len(np.unique(image))
    vals = 2 ** np.ceil(np.log2(vals))
    noisy = np.random.poisson(image.astype(np.float32) * vals) / float(vals)
    return np.clip(noisy, 0, 255).astype(np.uint8)

# 输入输出路径
#TODO
input_image_dir = r"C:\Users\Administrator\Desktop\inputDIR\images"
input_label_dir = r"C:\Users\Administrator\Desktop\inputDIR\labels"
output_base_dir = r"C:\Users\Administrator\Desktop\outputDIR"

# 创建输出目录
noise_types = ["gaussian", "snp", "poisson"]
for noise in noise_types:
    os.makedirs(os.path.join(output_base_dir, noise, "images"), exist_ok=True)
    os.makedirs(os.path.join(output_base_dir, noise, "labels"), exist_ok=True)

# 批量处理图像和标签
for filename in os.listdir(input_image_dir):
    if filename.lower().endswith(('.jpg','.png', '.jpeg')):
        name_no_ext = os.path.splitext(filename)[0]
        img_path = os.path.join(input_image_dir, filename)
        label_path = os.path.join(input_label_dir, name_no_ext + ".txt")
        img = cv2.imread(img_path)

        # 高斯噪声
        img_g = add_gaussian_noise(img)
        cv2.imwrite(os.path.join(output_base_dir, "gaussian", "images", f"{name_no_ext}_g.jpg"), img_g)
        if os.path.exists(label_path):
            shutil.copy(label_path, os.path.join(output_base_dir, "gaussian", "labels", f"{name_no_ext}_g.txt"))

        # 椒盐噪声
        img_snp = add_salt_pepper_noise(img, amount=0.005)
        cv2.imwrite(os.path.join(output_base_dir, "snp", "images", f"{name_no_ext}_snp.jpg"), img_snp)
        if os.path.exists(label_path):
            shutil.copy(label_path, os.path.join(output_base_dir, "snp", "labels", f"{name_no_ext}_snp.txt"))

        # 泊松噪声
        img_p = add_poisson_noise(img)
        cv2.imwrite(os.path.join(output_base_dir, "poisson", "images", f"{name_no_ext}_p.jpg"), img_p)
        if os.path.exists(label_path):
            shutil.copy(label_path, os.path.join(output_base_dir, "poisson", "labels", f"{name_no_ext}_p.txt"))
