import os
import subprocess
import json
import glob
import time
import datetime
import sys

# ================= CONFIGURATION =================
# 1. 核心路径配置 (OneDrive)
# 修正 ROOT_DIR 为 Inbox 所在位置
ROOT_DIR = r"C:\Users\王波\OneDrive\my_system\Inbox"
# 源文件仍在 D 盘
ENEX_DIR = r"D:\My_System\Inbox\Enex_Flat"
# 最终产物目录
OUTPUT_DIR = os.path.join(ROOT_DIR, "Yarle_Output_Final") 
# 模板文件在 my_system 根目录下，不在 Inbox 内
TEMPLATE_PATH = r"C:\Users\王波\OneDrive\my_system\obsidian_template.md"
LOG_FILE = os.path.join(ROOT_DIR, "migration_log.txt")

# 2. 超时设置 (防卡死)
TIMEOUT_SECONDS = 120  # 如果单文件处理超过 2 分钟，强制跳过
# 使用 npx 调用确保环境兼容
YARLE_CMD = "npx -y yarle-evernote-to-md"

# ================= UTILS =================
def log_message(message):
    """同时打印到控制台和日志文件"""
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    formatted_msg = f"[{timestamp}] {message}"
    # 写入文件
    try:
        with open(LOG_FILE, "a", encoding="utf-8") as f:
            f.write(formatted_msg + "\n")
    except Exception as e:
        pass # 无法写日志时不中断
    return formatted_msg

def format_time(seconds):
    """将秒数转换为 H:M:S"""
    return str(datetime.timedelta(seconds=int(seconds)))

# ================= MAIN LOGIC =================
def main():
    # 1. 初始化环境
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)
    
    # 确保日志文件目录存在
    if not os.path.exists(os.path.dirname(LOG_FILE)):
        os.makedirs(os.path.dirname(LOG_FILE))

    print("\n" + "="*50)
    print("🚀 JARVIS MEMORY MIGRATION - FINAL BATCH (V5)")
    print(f"📂 Source: {ENEX_DIR}")
    print(f"📂 Target: {OUTPUT_DIR}")
    print("="*50 + "\n")

    # 2. 扫描文件
    all_enex_files = glob.glob(os.path.join(ENEX_DIR, "*.enex"))
    total_files = len(all_enex_files)
    
    if total_files == 0:
        print("❌ Error: No .enex files found!")
        return

    # 3. 进度计算与断点检测
    start_time = time.time()
    processed_count = 0
    skipped_count = 0
    error_count = 0
    
    print(f"📊 Total Files Detected: {total_files}")
    log_message(f"=== Batch Started. Total: {total_files} ===")

    for index, enex_path in enumerate(all_enex_files):
        current_num = index + 1
        file_name = os.path.basename(enex_path)
        
        # --- 进度条显示 ---
        elapsed = time.time() - start_time
        avg_time = elapsed / (current_num) if current_num > 0 else 0
        remaining_files = total_files - current_num
        eta = remaining_files * avg_time
        
        percent = (current_num / total_files) * 100
        
        # 动态刷新行
        try:
            status_msg = (
                f"\r⏳ Progress: [{current_num}/{total_files}] {percent:.1f}% | "
                f"ETA: {format_time(eta)} | "
                f"Processing: {file_name[:20]}..."
            )
            sys.stdout.write(status_msg)
            sys.stdout.flush()
        except:
            pass

        # --- 生成配置 ---
        config_data = {
            "enexSources": [enex_path],
            "outputDir": OUTPUT_DIR,
            "templateFile": TEMPLATE_PATH,
            "isMetadataNeeded": True,
            "skipCreationTime": False,
            "skipUpdateTime": False,
            "dateFormat": "YYYY-MM-DD HH:mm:ss", 
            "nestedTags": {
                "separatorInEN": "/",
                "replaceSeparatorWith": "/"
            },
            "useHashTags": True,
            "keepOriginalHtml": False # 保持纯净 Markdown
        }
        
        # 使用唯一命名的配置文件，防止并行或快速切换时的冲突（虽然这里是串行）
        config_path = os.path.join(ROOT_DIR, "temp_config_v5.json")
        try:
            with open(config_path, "w", encoding="utf-8") as f:
                json.dump(config_data, f, indent=4, ensure_ascii=False)
        except Exception as e:
            error_count += 1
            sys.stdout.write("\n")
            log_message(f"❌ CONFIG ERROR: {file_name} | {str(e)}")
            continue

        # --- 执行转换 (带超时熔断) ---
        try:
            cmd = f'{YARLE_CMD} --configFile "{config_path}"'
            
            # 这里的 shell=True 在 Windows 是必须的
            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                encoding='utf-8',
                timeout=TIMEOUT_SECONDS, # <--- 核心：防卡死
                shell=True,
                env={**os.environ, "PYTHONIOENCODING": "utf-8"}
            )
            
            if result.returncode == 0:
                # 成功
                processed_count += 1
            else:
                error_count += 1
                sys.stdout.write("\n") # 换行显示错误
                # 尝试安全地解码错误信息
                err_msg = result.stderr[:200] if result.stderr else "Unknown Error"
                log_message(f"❌ FAILED: {file_name} | Err: {err_msg.replace(chr(10), ' ').replace(chr(13), '')}")
                
        except subprocess.TimeoutExpired:
            error_count += 1
            sys.stdout.write("\n") # 换行显示错误
            log_message(f"⚠️ TIMEOUT (SKIPPED): {file_name} took > {TIMEOUT_SECONDS}s")
            # 尝试清理可能残留的子进程（在 Windows 上 subprocess.run 超时通常能处理，但偶尔需要额外关注）
            
        except Exception as e:
            error_count += 1
            sys.stdout.write("\n")
            log_message(f"❌ ERROR: {file_name} | {str(e)}")
            
        # 简单的垃圾回收/清理
        if os.path.exists(config_path):
            try:
                os.remove(config_path)
            except:
                pass

    # 4. 结束汇总
    print("\n\n" + "="*50)
    print("✅ MIGRATION COMPLETED")
    print(f"Total: {total_files}")
    print(f"Success: {processed_count}")
    print(f"Errors/Skips: {error_count}")
    print(f"Log saved to: {LOG_FILE}")
    print("="*50)

if __name__ == "__main__":
    main()
