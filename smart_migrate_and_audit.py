import os
import shutil
import time
from pathlib import Path

def get_dir_size_and_count(path):
    """计算文件夹的总大小(bytes)和文件数量"""
    total_size = 0
    file_count = 0
    if not path.exists():
        return 0, 0
    
    for p in path.rglob('*'):
        if p.is_file():
            total_size += p.stat().st_size
            file_count += 1
    return total_size, file_count

def format_size(size_bytes):
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if size_bytes < 1024:
            return f"{size_bytes:.2f} {unit}"
        size_bytes /= 1024
    return f"{size_bytes:.2f} TB"

def find_onedrive_inbox():
    """动态寻找 OneDrive 下的 Inbox"""
    # 常用可能的路径
    user_home = Path.home()
    possible_paths = [
        user_home / "OneDrive - Personal" / "my_system" / "Inbox",
        user_home / "OneDrive" / "my_system" / "Inbox",
        Path(r"C:\Users\王波\OneDrive - Personal\my_system\Inbox") # 之前上下文得知的具体路径
    ]
    
    for p in possible_paths:
        if p.exists():
            return p
    return None

def main():
    print("\n-------------------------------------------------------------")
    print("🚀 Smart Migrate & Audit: 数据迁徙与熔断 (Jarvis Factory Protocol)")
    print("-------------------------------------------------------------\n")

    # --- 第一阶段：目标定义与环境侦测 ---
    print(">>> Phase 1: Pre-Flight Check (目标侦测)...\n")
    
    # 1. 定位源头
    source_inbox = find_onedrive_inbox()
    if not source_inbox:
        print("❌ [Error] 无法自动定位到 OneDrive 的 Inbox 目录。")
        print("请检查路径是否存在，或手动指定。")
        return

    targets = ["Enex_Flat", "Yarle_Output_Final"]
    migration_plan = []
    
    total_files_planned = 0
    total_size_planned = 0
    
    print(f"[*] 源目录定位: {source_inbox}")
    
    for target_name in targets:
        target_path = source_inbox / target_name
        if target_path.exists():
            size, count = get_dir_size_and_count(target_path)
            migration_plan.append({
                "name": target_name,
                "path": target_path,
                "size": size,
                "count": count
            })
            total_files_planned += count
            total_size_planned += size
            print(f"    - 发现目标: {target_name:<20} | 文件: {count:<5} | 大小: {format_size(size)}")
        else:
            print(f"    - 未找到目标: {target_name} (将跳过)")

    if total_files_planned == 0:
        print("\n⚠️ [Warning] 没有发现需要迁移的数据。任务终止。")
        return

    print(f"\n📢 【目标设定】预计迁移 {total_files_planned} 个文件，预计释放云空间 {format_size(total_size_planned)}")

    # 2. 规划终点
    if Path("D:/").exists():
        dest_root = Path("D:/Jarvis_Factory")
    else:
        dest_root = Path("C:/Jarvis_Factory")
    
    print(f"📢 【路径确认】\n    源: {source_inbox}\n    -> 目标: {dest_root}")

    # --- 第二阶段：执行大迁徙 ---
    print("\n" + "="*60)
    user_input = input("⏳ 按回车键开始执行迁移 (Enter to Start)，或 Ctrl+C 中止... ")
    print("="*60 + "\n")
    
    print(">>> Phase 2: Execution (开始执行)...\n")
    
    if not dest_root.exists():
        dest_root.mkdir(parents=True)
        print(f"[*] 创建目标根目录: {dest_root}")

    for item in migration_plan:
        src = item["path"]
        dst = dest_root / item["name"]
        
        # 冲突处理：如果目标已存在，重命名旧的
        if dst.exists():
            timestamp = int(time.time())
            backup_name = f"{item['name']}_backup_{timestamp}"
            dst_backup = dest_root / backup_name
            print(f"[*] 目标路径冲突，正在将旧数据重命名为: {backup_name}")
            dst.rename(dst_backup)
        
        print(f"[*] 正在移动: {item['name']} ...")
        try:
            shutil.move(str(src), str(dst))
            print(f"    ✅ 移动完成")
        except Exception as e:
            print(f"    ❌ 移动失败: {e}")
            # 如果失败，可能部分移动，这里为了脚本简单暂不回滚，但审计会发现差异

    # --- 第三阶段：目标检测与验收报告 ---
    print("\n>>> Phase 3: Post-Flight Audit (审计验收)...\n")
    
    input("⏳ 稍微等待文件系统同步... 按回车查看报告")
    
    actual_files = 0
    actual_size = 0
    source_cleared = True
    
    # 1. 源头复查
    for item in migration_plan:
        if item["path"].exists():
            print(f"❌ [Error] 源文件夹残留: {item['name']}")
            source_cleared = False
        else:
            # print(f"✅ 源文件夹已移除: {item['name']}")
            pass
            
    # 2. 终点核验
    for item in migration_plan:
        dst = dest_root / item["name"]
        if dst.exists():
            s, c = get_dir_size_and_count(dst)
            actual_size += s
            actual_files += c
        else:
            print(f"❌ [Error] 目标文件夹缺失: {item['name']}")

    # 3. 最终反馈
    integrity_match = (actual_files == total_files_planned) and (abs(actual_size - total_size_planned) < 1024*1024) # 允许1MB误差
    
    print("\n" + "-"*50)
    print("📊 迁移审计报告 (Migration Audit Report)")
    print("-"*50)
    print(f"1. [目标] 计划迁移文件数：{total_files_planned:<8} | 计划释放空间：{format_size(total_size_planned)}")
    print(f"2. [结果] 实际抵达文件数：{actual_files:<8} | 实际占用空间：{format_size(actual_size)}")
    
    status_icon = "✅ 100%" if integrity_match else "⚠️ 数据不一致"
    print(f"3. [状态] 数据完整性：{status_icon}")
    
    cloud_status = "✅ 成功" if source_cleared else "❌ 还有残留"
    print(f"4. [云端] OneDrive 空间释放：{cloud_status}")
    print("-"*50)
    
    if integrity_match and source_cleared:
        print("\n🎉 任务圆满完成。一切都在掌控之中。")
    else:
        print("\n⚠️ 任务完成但存在异常，请检查上述错误日志。")

if __name__ == "__main__":
    main()
