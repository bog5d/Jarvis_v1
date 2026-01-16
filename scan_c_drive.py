import os
import re
from pathlib import Path

# 配置扫描路径 (针对用户的 Home 目录)
SEARCH_ROOT = Path(r"C:\Users\王波")
# 设置大文件阈值 (100MB)
MIN_SIZE_MB = 100
MIN_SIZE_BYTES = MIN_SIZE_MB * 1024 * 1024

def get_size_str(size_in_bytes):
    for unit in ['B', 'KB', 'MB', 'GB']:
        if size_in_bytes < 1024:
            return f"{size_in_bytes:.2f} {unit}"
        size_in_bytes /= 1024
    return f"{size_in_bytes:.2f} TB"

def is_safe_to_delete(file_path):
    """基于路径和后缀推测是否可以安全删除"""
    path_str = str(file_path).lower()
    name = file_path.name.lower()
    suffix = file_path.suffix.lower()

    # 1. 下载目录中的安装包或压缩文件
    if "downloads" in path_str:
        if suffix in ['.exe', '.msi', '.zip', '.rar', '.7z', '.iso']:
            return True, "下载的安装包/压缩包"

    # 2. 临时文件
    if "temp" in path_str or "tmp" in path_str:
        return True, "临时文件"
        
    # 3. 可能是解压后的全部 Evernote 数据 (Context)
    if "enex_export" in path_str or "enex_flat" in path_str or "yarle" in path_str:
        return True, "Evernote/Jarvis 中间过程数据"

    # 4. 压缩包备份
    if suffix in ['.zip', '.rar', '.7z', '.tar', '.gz']:
        return True, "压缩包 (可能是备份)"
        
    # 5. 日志文件
    if suffix in ['.log', '.dmp']:
        return True, "日志/转储文件"

    return False, "未知类型 (谨慎删除)"

def scan_c_drive():
    print(f"正在扫描 {SEARCH_ROOT} 下大于 {MIN_SIZE_MB}MB 的文件...")
    print("这可能需要几分钟，请耐心等待...\n")
    
    large_files = []
    
    # 排除一些必定不该动的目录以加快速度和减少噪音
    exclude_dirs = {'.git', '.vscode', 'AppData\\Local\\Microsoft', 'AppData\\Roaming\\Microsoft'}

    try:
        for root, dirs, files in os.walk(SEARCH_ROOT):
            # 剪枝
            dirs[:] = [d for d in dirs if d not in exclude_dirs]
            
            for name in files:
                try:
                    file_path = Path(root) / name
                    
                    # 跳过软链接
                    if file_path.is_symlink():
                        continue
                        
                    stat = file_path.stat()
                    size = stat.st_size
                    
                    if size > MIN_SIZE_BYTES:
                        safe, reason = is_safe_to_delete(file_path)
                        large_files.append({
                            'path': str(file_path),
                            'size': size,
                            'safe': safe,
                            'reason': reason
                        })
                except (PermissionError, OSError):
                    pass 
                    
    except KeyboardInterrupt:
        print("\n扫描已中断。")
    
    # 按大小降序排列
    large_files.sort(key=lambda x: x['size'], reverse=True)
    
    print("-" * 100)
    print(f"{'状态':<10} {'大小':<10} {'说明':<25} {'文件路径'}")
    print("-" * 100)
    
    # 只显示前 30 个最大的
    count = 0
    for item in large_files:
        if count >= 30:
            break
            
        status = "[建议删除]" if item['safe'] else "[需确认]"
        # 截断过长的路径显示
        display_path = item['path'] if len(item['path']) < 60 else "..." + item['path'][-55:]
        
        print(f"{status:<10} {get_size_str(item['size']):<10} {item['reason']:<25} {display_path}")
        count += 1

    print("-" * 100)
    print(f"\n共发现 {len(large_files)} 个大文件。")

if __name__ == "__main__":
    scan_c_drive()
