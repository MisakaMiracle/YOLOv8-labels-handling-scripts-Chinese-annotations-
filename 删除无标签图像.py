import os

# 设置路径
#TODO
image_dir = r"C:\Users\Administrator\Desktop\DirName\images"   # 图像路径
label_dir = r"C:\Users\Administrator\Desktop\DirName\labels"   # 标签路径

# 支持的图像扩展名
image_exts = {'.jpg', '.jpeg', '.png', '.bmp', '.webp'}

# 遍历图像文件
for filename in os.listdir(image_dir):
    name, ext = os.path.splitext(filename)
    
    if ext.lower() not in image_exts:
        continue  # 跳过非图像文件
    
    image_path = os.path.join(image_dir, filename)
    label_path = os.path.join(label_dir, f"{name}.txt")

    # 如果对应标签文件不存在，删除图像
    if not os.path.isfile(label_path):
        print(f"❌ 删除无标签图像: {filename}")
        os.remove(image_path)
    else:
        print(f"✅ 保留: {filename}")

print("完成。")