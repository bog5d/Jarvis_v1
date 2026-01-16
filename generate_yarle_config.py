import os
import json
import glob

ENEX_DIR = r"C:\Users\王波\OneDrive - Personal\my_system\Inbox\Enex_Ready"
TEMPLATE_FILE = r"C:\Users\王波\OneDrive - Personal\my_system\Jarvis_v1\config\yarle_template.md"
OUTPUT_DIR = r"C:\Users\王波\OneDrive - Personal\my_system\Inbox\Yarle_Output"
CONFIG_OUTPUT = r"C:\Users\王波\OneDrive - Personal\my_system\Jarvis_v1\config\yarle_config_generated.json"

def generate_config():
    # Get all .enex files
    enex_files = glob.glob(os.path.join(ENEX_DIR, "*.enex"))
    # Normalize paths for JSON (double backslashes are handled by json.dump)
    enex_files = [f for f in enex_files]
    
    config = {
        "enexSources": enex_files,
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
        "skipEnexFileNameFromOutputPath": False,
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
    
    print(f"Generated config with {len(enex_files)} source files at: {CONFIG_OUTPUT}")

if __name__ == "__main__":
    generate_config()
