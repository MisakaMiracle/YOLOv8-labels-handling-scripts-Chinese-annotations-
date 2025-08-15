import os
#重命名指定文件夹下的图像为background_1.jpg,background_2.jpg,background_3.jpg......
#Rename files as background_1.jpg,background_2.jpg,background_3.jpg......
# 指定要重命名的文件夹路径
#TODO
folder_path = r"C:\Users\Administrator\Desktop\DIR"  # 例如 r"C:\Users\YourName\Pictures"

# 获取该文件夹下所有文件
file_list = os.listdir(folder_path)

# 只保留文件（排除文件夹），并排序（可选）
file_list = [f for f in file_list if os.path.isfile(os.path.join(folder_path, f))]
file_list.sort()

# 遍历并重命名
for index, filename in enumerate(file_list, start=1):
    # 获取文件扩展名（保留原始扩展名也可以，但此处强制改为.jpg）
    new_name = f"background_{index}.jpg"
    old_path = os.path.join(folder_path, filename)
    new_path = os.path.join(folder_path, new_name)
    os.rename(old_path, new_path)

print("重命名完成！")
