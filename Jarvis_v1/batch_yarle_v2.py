import os
import json
import subprocess
import glob
import time

ENEX_DIR = r"D:\My_System\Inbox\Enex_Flat"
OUTPUT_DIR = r"D:\My_System\Inbox\Yarle_Output_Final"

# Yarle 配置模板
CONFIG_TEMPLATE = {
    "outputDir": OUTPUT_DIR,
    "isMetadataNeeded": True,
    "isNotebookNameNeeded": True,
    "isZettelkastenNeeded": False,
    "useHashTags": True,
    "outputFormat": "ObsidianMD",
    "skipWebClips": False,
    "isSmallestImageSizeNeeded": True,
    "trimTitle": True,
    "replaceSpacesInTags": True,
    "dateFormat": "YYYY-MM-DD",
    "resourcesDir": "_resources",
    "nestedTags": {
        "separatorInEN": "/",
        "replaceSeparatorWith": "/"
    }
}

def main():
    # 确保输出目录存在
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    # 获取所有 Enex 文件
    enex_files = glob.glob(os.path.join(ENEX_DIR, "*.enex"))
    total = len(enex_files)
    print(f"Total files to process: {total}")

    success_count = 0
    fail_count = 0

    # 临时配置文件名
    temp_config_path = os.path.abspath(f"yarle_config_temp_v2.json")

    for i, file_path in enumerate(enex_files):
        filename = os.path.basename(file_path)
        print(f"\n[{i+1}/{total}] Processing: {filename}")
        
        # 针对每个文件生成一个临时 Config
        # 必须使用绝对路径
        current_config = CONFIG_TEMPLATE.copy()
        current_config["enexSources"] = [file_path]
        
        with open(temp_config_path, "w", encoding="utf-8") as f:
            json.dump(current_config, f, indent=2, ensure_ascii=False)
            
        # 构造命令
        # 注意：在 Windows 上 npx 最好用 shell=True 执行
        cmd = f'npx -y yarle-evernote-to-md --configFile "{temp_config_path}"'
        
        try:
            # 增加内存限制
            env = os.environ.copy()
            env["NODE_OPTIONS"] = "--max-old-space-size=4096"
            
            subprocess.run(cmd, check=True, shell=True, env=env)
            success_count += 1
            print(f"Success: {filename}")
        except subprocess.CalledProcessError as e:
            fail_count += 1
            print(f"Error processing {filename}: {e}")
        except Exception as e:
            fail_count += 1
            print(f"Unexpected error: {e}")
            
    # 清理临时文件
    if os.path.exists(temp_config_path):
        try:
            os.remove(temp_config_path)
        except:
            pass

    print("\n" + "="*30)
    print(f"Batch Processing Complete!")
    print(f"Total: {total}, Success: {success_count}, Failed: {fail_count}")
    print(f"Output Directory: {OUTPUT_DIR}")

if __name__ == "__main__":
    main()
