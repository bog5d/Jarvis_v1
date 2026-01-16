import os
import json
import glob

# 配置路径
ENEX_DIR = r"C:\Users\王波\OneDrive - Personal\my_system\Inbox\Enex_Flat"
OUTPUT_DIR = r"C:\Users\王波\OneDrive - Personal\my_system\Inbox\Yarle_Output_Final"
CONFIG_PATH = r"C:\Users\王波\OneDrive - Personal\my_system\Jarvis_v1\config\yarle_config_auto.json"

def main():
    # 1. 获取所有 Enex 文件路径
    enex_files = glob.glob(os.path.join(ENEX_DIR, "*.enex"))
    
    if not enex_files:
        print(f"错误: 在 {ENEX_DIR} 中没有找到 .enex 文件")
        return

    print(f"找到 {len(enex_files)} 个 Enex 文件。")

    # 2. 构建 Yarle 配置
    config = {
        "enexSources": enex_files,
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
        },
        "logPath": r"D:\My_System\Inbox\yarle_conversion.log"
    }

    # 3. 写入文件
    try:
        # 确保目录存在
        os.makedirs(os.path.dirname(CONFIG_PATH), exist_ok=True)
        
        with open(CONFIG_PATH, 'w', encoding='utf-8') as f:
            json.dump(config, f, indent=4, ensure_ascii=False)
        
        print(f"配置文件已生成: {CONFIG_PATH}")
        print(f"输出目录设置为: {OUTPUT_DIR}")
        
    except Exception as e:
        print(f"写入配置文件失败: {e}")

if __name__ == "__main__":
    main()
