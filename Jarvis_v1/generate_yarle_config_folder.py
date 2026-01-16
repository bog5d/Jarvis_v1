import os
import json

ENEX_DIR = r"D:\My_System\Inbox\Enex_Ready"
TEMPLATE_FILE = r"D:\My_System\Jarvis_v1\config\yarle_template.md"
OUTPUT_DIR = r"D:\My_System\Inbox\Yarle_Output"
CONFIG_OUTPUT = r"D:\My_System\Jarvis_v1\config\yarle_config_folder.json"

def generate_config():
    # Pass the DIRECTORY not the files
    config = {
        "enexSources": [ENEX_DIR], 
        "outputDir": OUTPUT_DIR,
        "isMetadataNeeded": True,
        "isNotebookNameNeeded": True,
        "isZettelkastenNeeded": False,
        "useZettelIdAsFilename": False,
        "plainTextNotesOnly": False,
        "skipLocation": True,
        "skipCreationTime": False,
        "skipUpdateTime": False,
        "skipSourceUrl": False,
        "skipWebClips": False,
        "skipTags": False,
        "useHashTags": True,
        "outputFormat": "ObsidianMD",
        "skipEnexFileNameFromOutputPath": False, # Important to keep organization
        "keepMDCharactersOfENNotes": False,
        "monospaceIsCodeBlock": True,
        "keepOriginalHtml": False,
        "nestedTags": {
            "separatorInEN": "/",
            "replaceSeparatorWith": "/"
        },
        "resourcesDir": "_resources",
        "turndownOptions": {
            "headingStyle": "atx"
        },
        "templateFile": TEMPLATE_FILE
    }
    
    with open(CONFIG_OUTPUT, 'w', encoding='utf-8') as f:
        json.dump(config, f, indent=4, ensure_ascii=False)
    
    print(f"Generated folder-based config at: {CONFIG_OUTPUT}")

if __name__ == "__main__":
    generate_config()
