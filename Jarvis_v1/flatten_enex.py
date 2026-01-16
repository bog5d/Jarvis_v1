import os
import shutil
import re
import sys

# 设置输入输出目录
SOURCE_DIR = r"D:\My_System\Inbox\Enex_Export"
TARGET_DIR = r"D:\My_System\Inbox\Enex_Flat"

def sanitize(name):
    """
    清理文件名，将不友好的字符（空格、等号、特殊符号）替换为下划线。
    保留中文、字母、数字、点。
    """
    # 替换空格、tab
    name = re.sub(r'\s+', '_', name)
    # 替换 Windows 文件名非法字符: < > : " / \ | ? *
    # 以及可能干扰命令行的字符: = ( ) [ ]
    name = re.sub(r'[<>:"/\\|?*=\(\)\[\]]', '_', name)
    # 消除重复的下划线
    name = re.sub(r'_+', '_', name)
    # 去除首尾下划线
    name = name.strip('_')
    return name

def main():
    print(f"准备开始处理...")
    print(f"源目录: {SOURCE_DIR}")
    print(f"目标目录: {TARGET_DIR}")

    if not os.path.exists(SOURCE_DIR):
        print(f"错误: 源目录不存在 {SOURCE_DIR}")
        return

    if not os.path.exists(TARGET_DIR):
        try:
            os.makedirs(TARGET_DIR)
            print(f"已创建目标目录: {TARGET_DIR}")
        except Exception as e:
            print(f"无法创建目标目录: {e}")
            return

    count = 0
    total_size = 0
    
    # 遍历所有文件
    for root, dirs, files in os.walk(SOURCE_DIR):
        for file in files:
            if file.lower().endswith('.enex'):
                source_path = os.path.join(root, file)
                
                # 计算相对路径，用于生成前缀
                rel_path = os.path.relpath(root, SOURCE_DIR)
                
                if rel_path == '.':
                    # 就在根目录下
                    base_name = os.path.splitext(file)[0]
                    new_name_base = sanitize(base_name)
                else:
                    # 在子文件夹里，把文件夹名也加进去作为前缀
                    # 例如 "01= 每日收集组" -> "01_每日收集组"
                    folder_name = sanitize(rel_path)
                    file_name = os.path.splitext(file)[0]
                    file_name_clean = sanitize(file_name)
                    new_name_base = f"{folder_name}__{file_name_clean}"
                
                new_filename = f"{new_name_base}.enex"
                target_path = os.path.join(TARGET_DIR, new_filename)
                
                # 检查文件大小
                file_size = os.path.getsize(source_path)
                total_size += file_size
                
                print(f"[{count+1}] 复制: ...{file[-20:] if len(file)>20 else file} -> {new_filename}")
                
                try:
                    # 使用 copy2 保留元数据
                    shutil.copy2(source_path, target_path)
                    count += 1
                except Exception as e:
                    print(f"  复制失败: {e}")

    print("-" * 50)
    print(f"处理完成!")
    print(f"共处理文件: {count} 个")
    print(f"总数据量: {total_size / (1024*1024*1024):.2f} GB")

if __name__ == "__main__":
    main()
