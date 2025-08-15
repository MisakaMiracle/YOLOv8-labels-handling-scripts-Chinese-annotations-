import os
'''
例如当前目录下某个叫"A1.txt"的标签文件内容为
“
1 0.201141 0.478340 0.072421 0.116733
0 0.267609 0.498512 0.040179 0.040675
0 0.395585 0.549107 0.037698 0.030093
”

你需要将
“1 0.201141 0.478340 0.072421 0.116733”
提取到./a/A1.txt中，

然后需要将
“
0 0.267609 0.498512 0.040179 0.040675
0 0.395585 0.549107 0.037698 0.030093
”
提取到./b/A1.txt中。
'''
# 源标签文件所在目录
#TODO
label_dir = r"C:\Users\Administrator\Desktop\DirName\labels"   # 这里改成你的标签文件路径
# 分类后的保存目录
a_dir = r"C:\Users\Administrator\Desktop\dai_Work\labels0"  # 存放第一列为 0 的行
b_dir = r"C:\Users\Administrator\Desktop\dai_Work\labels1"  # 存放第一列为 1 的行

# 确保目标目录存在
os.makedirs(a_dir, exist_ok=True)
os.makedirs(b_dir, exist_ok=True)

# 遍历目录中的所有标签文件
for filename in os.listdir(label_dir):
    if not filename.endswith(".txt"):
        continue

    file_path = os.path.join(label_dir, filename)
    with open(file_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    # 分别保存不同类别的行
    lines_class_0 = []
    lines_class_1 = []
    for line in lines:
        parts = line.strip().split()
        if not parts:
            continue
        if parts[0] == "0":
            lines_class_0.append(line)
        elif parts[0] == "1":
            lines_class_1.append(line)

    # 写入 ./a （类别 0 的行）
    if lines_class_0:
        with open(os.path.join(a_dir, filename), "w", encoding="utf-8") as f:
            f.writelines(lines_class_0)

    # 写入 ./b （类别 1 的行）
    if lines_class_1:
        with open(os.path.join(b_dir, filename), "w", encoding="utf-8") as f:
            f.writelines(lines_class_1)

print("处理完成！")
