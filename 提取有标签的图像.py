import os
import shutil
#提取有标签文件的图像
# === 路径设置 ===
#TODO
label_dir = r"C:\path\to\labels"        # YOLOv8 标注文件所在目录
image_dir = r"C:\path\to\images"        # 所有图像所在目录
output_dir = r"C:\path\to\output"       # 提取图像的目标目录

# === 支持的图像扩展名 ===
image_extensions = [".jpg", ".jpeg", ".png"]

# 创建输出目录（如果不存在）
os.makedirs(output_dir, exist_ok=True)

# 遍历所有标签文件
for label_file in os.listdir(label_dir):
    if not label_file.endswith(".txt"):
        continue

    # 去掉.txt扩展名
    base_name = os.path.splitext(label_file)[0]

    # 在图像目录中查找同名图像
    for ext in image_extensions:
        image_file = base_name + ext
        image_path = os.path.join(image_dir, image_file)

        if os.path.exists(image_path):
            # 复制图像到目标目录
            shutil.copy(image_path, os.path.join(output_dir, image_file))
            print(f"已复制：{image_file}")
            break  # 找到一个匹配的图像就跳出循环

print("处理完成！")
