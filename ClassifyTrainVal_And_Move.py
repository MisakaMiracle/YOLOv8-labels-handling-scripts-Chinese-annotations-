import os
import random
import shutil

#将图像放到./images下，将标签放到./labels下

def split_dataset(base_dir, train_ratio=0.9):               #训练集、验证集比例9：1
    image_dir = os.path.join(base_dir, "images")
    label_dir = os.path.join(base_dir, "labels")

    # 输出子目录
    image_train_dir = os.path.join(image_dir, "train")
    image_val_dir = os.path.join(image_dir, "val")
    label_train_dir = os.path.join(label_dir, "train")
    label_val_dir = os.path.join(label_dir, "val")

    # 创建输出目录
    os.makedirs(image_train_dir, exist_ok=True)
    os.makedirs(image_val_dir, exist_ok=True)
    os.makedirs(label_train_dir, exist_ok=True)
    os.makedirs(label_val_dir, exist_ok=True)

    # 获取所有 image 文件名（不包含子文件夹）
    image_files = [f for f in os.listdir(image_dir) if f.lower().endswith(('.jpg', '.jpeg', '.png')) and os.path.isfile(os.path.join(image_dir, f))]

    # 打乱顺序并划分
    random.shuffle(image_files)
    train_size = int(len(image_files) * train_ratio)
    train_images = image_files[:train_size]
    val_images = image_files[train_size:]

    # 处理训练集图像和标签
    for img in train_images:
        base_name = os.path.splitext(img)[0]
        img_path = os.path.join(image_dir, img)
        lbl_path = os.path.join(label_dir, base_name + ".txt")

        shutil.move(img_path, os.path.join(image_train_dir, img))
        if os.path.exists(lbl_path):
            shutil.move(lbl_path, os.path.join(label_train_dir, base_name + ".txt"))

    # 处理验证集图像和标签
    for img in val_images:
        base_name = os.path.splitext(img)[0]
        img_path = os.path.join(image_dir, img)
        lbl_path = os.path.join(label_dir, base_name + ".txt")

        shutil.move(img_path, os.path.join(image_val_dir, img))
        if os.path.exists(lbl_path):
            shutil.move(lbl_path, os.path.join(label_val_dir, base_name + ".txt"))

    print(f"✅ 分割完成：训练集 {len(train_images)} 张，验证集 {len(val_images)} 张")

# 示例调用（替换为你的实际路径）（images和labels的父文件夹）
#TODO
split_dataset(r"C:\Users\Administrator\Desktop\DirName")
