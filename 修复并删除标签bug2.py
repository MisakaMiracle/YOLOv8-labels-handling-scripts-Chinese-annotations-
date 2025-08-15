import os
import subprocess

def is_bad_label_file(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            for line in f:
                parts = line.strip().split()
                if len(parts) != 5:
                    return True
        return False
    except Exception:
        # 无法读取也认为是坏文件
        return True

def force_delete_file(filepath):
    try:
        cmd = ['powershell', '-Command', f'Remove-Item -Path "{filepath}" -Force']
        subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        print(f"已强制删除格式错误文件: {filepath}")
    except subprocess.CalledProcessError:
        print(f"无法删除文件（可能被占用）: {filepath}")

def batch_delete_bad_labels(folder_path):
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            full_path = os.path.join(root, file)
            if is_bad_label_file(full_path):
                force_delete_file(full_path)

if __name__ == "__main__":
    #TODO
    target_folder = r"C:\Users\Administrator\Desktop\DirName\labels"  # 替换为你的标签文件夹路径
    batch_delete_bad_labels(target_folder)
