import os
import subprocess
import json
import glob
import sys

# ================= CONFIGURATION =================
# Since OneDrive/Inbox/Enex_Flat does not exist or is empty, we use the D: drive source
ROOT_DIR = r"C:\Users\王波\OneDrive\my_system" # Using root logic structure
ENEX_DIR = r"D:\My_System\Inbox\Enex_Flat" 
OUTPUT_DIR = os.path.join(ROOT_DIR, "inbox", "Yarle_Output_Pilot_V4")
TEMPLATE_PATH = os.path.join(ROOT_DIR, "obsidian_template.md")

# Use npx directly as before
YARLE_CMD = "npx -y yarle-evernote-to-md" 

# ================= MAIN LOGIC =================
def run_pilot():
    # 确保输出目录存在
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)
        print(f"[Init] Created output dir: {OUTPUT_DIR}")

    # 获取所有 .enex 文件
    enex_files = glob.glob(os.path.join(ENEX_DIR, "*.enex"))
    
    if not enex_files:
        print(f"[Error] No .enex files found in {ENEX_DIR}")
        return

    # !!! 仅取前 5 个文件进行测试 !!!
    pilot_batch = enex_files[:5]
    print(f"[Pilot] Selected {len(pilot_batch)} files for testing (Target: 5).")

    for index, enex_path in enumerate(pilot_batch):
        file_name = os.path.basename(enex_path)
        print(f"\n[{index+1}/5] Processing: {file_name}")

        # 生成临时的 yarle 配置文件 (config.json)
        config_data = {
            "enexSources": [enex_path],
            "outputDir": OUTPUT_DIR,
            "templateFile": TEMPLATE_PATH,
            "isMetadataNeeded": True,
            "skipCreationTime": False, # 确保不跳过创建时间
            "skipUpdateTime": False,
            "dateFormat": "YYYY-MM-DD HH:mm:ss", # 强制时间格式
            "nestedTags": {
                "separatorInEN": "/",
                "replaceSeparatorWith": "/"
            },
            "useHashTags": True
        }

        config_path = os.path.join(ROOT_DIR, "temp_config.json")
        
        try:
            with open(config_path, "w", encoding="utf-8") as f:
                json.dump(config_data, f, indent=4, ensure_ascii=False)
            
            # 构造命令
            cmd = f'{YARLE_CMD} --configFile "{config_path}"'
            
            # 调用 Windows 的 cmd
            result = subprocess.run(
                cmd, 
                capture_output=True, 
                text=True, 
                encoding='utf-8',
                shell=True,
                env={**os.environ, "PYTHONIOENCODING": "utf-8"}
            )

            if result.returncode == 0:
                print(f"✅ Success: {file_name}")
            else:
                print(f"❌ Failed: {file_name}")
                # Try to print stderr, handling potential encoding issues
                try:
                    print(f"   Error Log: {result.stderr}")
                except:
                    print(f"   Error Log (Raw): {result.stderr.encode('utf-8', errors='ignore')}")

        except Exception as e:
            print(f"❌ Exception: {str(e)}")

    print("\n" + "="*30)
    print("Pilot Run Complete.")
    print(f"Please check content in: {OUTPUT_DIR}")
    print("Verify: 1. Date format (2023-xx-xx) 2. No Chinese Mojibake")

if __name__ == "__main__":
    run_pilot()
