import os
import shutil

# 修改这两个路径为你自己的路径
#TODO
source_folder = r"C:\Users\Administrator\Desktop\aaa"
target_folder = r"C:\Users\Administrator\Desktop\bbb"

# 支持的图片扩展名（小写）
image_extensions = {'.jpg', '.jpeg', '.png', '.bmp', '.gif', '.tiff', '.webp'}

def is_image_file(filename):
    return os.path.splitext(filename)[1].lower() in image_extensions

def copy_images_recursively(src_dir, dst_dir):
    if not os.path.exists(dst_dir):
        os.makedirs(dst_dir)

    counter = 1
    for root, _, files in os.walk(src_dir):
        for file in files:
            if is_image_file(file):
                src_path = os.path.join(root, file)
                filename = os.path.basename(file)
                dst_path = os.path.join(dst_dir, filename)

                # 如果目标文件名已存在，则自动重命名
                while os.path.exists(dst_path):
                    name, ext = os.path.splitext(filename)
                    dst_path = os.path.join(dst_dir, f"{name}_{counter}{ext}")
                    counter += 1

                shutil.copy2(src_path, dst_path)
                print(f"复制: {src_path} -> {dst_path}")

if __name__ == "__main__":
    copy_images_recursively(source_folder, target_folder)
    print("图片复制完成。")
