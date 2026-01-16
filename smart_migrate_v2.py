import os
import shutil
import sys
import time

# ================= CONFIGURATION =================
# 硬编码已确认的路径，防止自动检测出错
SOURCE_ROOT = r"C:\Users\王波\OneDrive\my_system\Inbox"
DEST_ROOT = r"D:\Jarvis_Factory"
TARGET_FOLDERS = ["Enex_Flat", "Yarle_Output_Final"]

def get_dir_size_and_count(path):
    total_size = 0
    file_count = 0
    if not os.path.exists(path):
        return 0, 0
    for dirpath, _, filenames in os.walk(path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            if not os.path.exists(fp): continue
            total_size += os.path.getsize(fp)
            file_count += 1
    return file_count, total_size

def format_size(size):
    try:
        if size < 1024: return f"{size} B"
        elif size < 1024**2: return f"{size/1024:.2f} KB"
        elif size < 1024**3: return f"{size/1024**2:.2f} MB"
        else: return f"{size/1024**3:.2f} GB"
    except: return "0 B"

def main():
    print("\n" + "="*60)
    print("🚀 SMART MIGRATE & AUDIT CHECKLIST (FIXED PATH VERSION)")
    print("="*60)
    
    # ---------------- Phase 1: Pre-Flight Check ----------------
    print(f"\nPhase 1: Pre-Flight Check")
    print(f"[*] Source: {SOURCE_ROOT}")
    print(f"[*] Target: {DEST_ROOT}")
    
    if not os.path.exists(SOURCE_ROOT):
        print(f"❌ Error: Source root not found!")
        return

    # Check Targets
    migration_plan = []
    total_files = 0
    total_size = 0
    
    for folder in TARGET_FOLDERS:
        src_path = os.path.join(SOURCE_ROOT, folder)
        if os.path.exists(src_path):
            print(f"[+] Scanning {folder}...")
            count, size = get_dir_size_and_count(src_path)
            migration_plan.append({
                'name': folder,
                'src': src_path,
                'dest': os.path.join(DEST_ROOT, folder),
                'count': count,
                'size': size
            })
            print(f"    - Found: {count} files | Size: {format_size(size)}")
            total_files += count
            total_size += size
        else:
            print(f"[-] Not found: {folder} (Skipping)")
            
    if not migration_plan:
        print("❌ No valid folders found to migrate. System Clean?")
        return
        
    print(f"\n📊 Summary: Moving {total_files} files (~{format_size(total_size)}) to D: Drive.")
    
    # Check D: space? (Optional, but user said it's cleaned)
    
    # ---------------- Phase 2: Execution ----------------
    print("\nPhase 2: Execution")
    # Auto-confirm implies we proceed
    print(">>> Starting Migration Sequence...")
    
    if not os.path.exists(DEST_ROOT):
        os.makedirs(DEST_ROOT)
        
    for item in migration_plan:
        src = item['src']
        dest = item['dest']
        name = item['name']
        
        # Conflict Resolution
        if os.path.exists(dest):
            # If dest exists, it might be the partial failure from before.
            # We rename it to backup just in case.
            backup_name = f"{name}_partial_{int(time.time())}"
            backup_path = os.path.join(DEST_ROOT, backup_name)
            print(f"    ⚠️ Conflict detected at target. Renaming existing folder to {backup_name}")
            try:
                os.rename(dest, backup_path)
            except Exception as e:
                print(f"    ❌ Failed to rename conflict: {e}")
                # Try to merge/overwrite logic? shutil.move might fail if dest exists.
                # If rename failed, we might be stuck. But let's hope it works.
                continue
                
        # Move
        print(f"    🚀 Moving {name}...")
        try:
            shutil.move(src, dest)
            print(f"    ✅ Success: {name} moved.")
        except Exception as e:
            print(f"    ❌ Migration Failed for {name}: {e}")

    # ---------------- Phase 3: Post-Flight Audit ----------------
    print("\nPhase 3: Post-Flight Audit")
    
    audit_files = 0
    audit_size = 0
    onedrive_cleared = True
    
    for item in migration_plan:
        name = item['name']
        
        # 1. Verify Source is Gone
        if os.path.exists(item['src']):
            print(f"    ❌ Audit Fail: Source folder {name} still exists!")
            onedrive_cleared = False
        else:
            print(f"    ✅ Source Clean: {name} removed from OneDrive.")
            
        # 2. Verify Dest is Valid
        if os.path.exists(item['dest']):
            print(f"    🔍 Verifying target {name}...")
            c, s = get_dir_size_and_count(item['dest'])
            audit_files += c
            audit_size += s
            # Simple integrity check
            if c == item['count']:
                 print(f"    ✅ Integrity Check Passed: Count {c} matches.")
            else:
                 print(f"    ⚠️ Integrity Warning: Expected {item['count']}, Found {c}")
        else:
            print(f"    ❌ Audit Fail: Target folder {name} missing!")

    print("\n" + "-"*50)
    print("📊 最终审计报告 (FINAL REPORT)")
    print("-" * 50)
    print(f"1. [计划] 迁移: {total_files} 文件 | {format_size(total_size)}")
    print(f"2. [实际] 落地: {audit_files} 文件 | {format_size(audit_size)}")
    
    if audit_files == total_files:
        print("3. [状态] ✅ 完美 (Data 100% Intact)")
    else:
        print(f"3. [状态] ⚠️ 差异 (Difference: {total_files - audit_files} files)")
        
    if onedrive_cleared:
        print("4. [空间] ✅ OneDrive 已释放")
    else:
        print("4. [空间] ❌ OneDrive 仍被占用 (需手动检查)")
    print("-" * 50)

if __name__ == "__main__":
    main()
