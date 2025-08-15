import os
#Modify the first column of the tag file to 0.
# 标签文件所在目录
#TODO
label_dir = r"C:\Users\Administrator\Desktop\DIR\labels"  # 改成你的路径

for filename in os.listdir(label_dir):
    if not filename.endswith(".txt"):
        continue

    file_path = os.path.join(label_dir, filename)

    with open(file_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    new_lines = []
    for line in lines:
        parts = line.strip().split()
        if not parts:
            continue
        parts[0] = "0"  # 强制修改第一列为 0
        new_lines.append(" ".join(parts) + "\n")

    # 覆盖写回文件
    with open(file_path, "w", encoding="utf-8") as f:
        f.writelines(new_lines)

print("所有标签文件的第一列已改为 0！")
