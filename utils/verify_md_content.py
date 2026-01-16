import os

# Path to the generated MD file
md_path = r"C:\Users\王波\OneDrive\my_system\inbox\Yarle_Output_Pilot_V4\演讲PPT大纲：时代孝廉树新风，清风朗月正青春.md"

if not os.path.exists(md_path):
    # Try finding any md file
    import glob
    files = glob.glob(r"C:\Users\王波\OneDrive\my_system\inbox\Yarle_Output_Pilot_V4\*.md", recursive=True)
    if files:
        md_path = files[0]
    else:
        print("No MD file found.")
        exit()

print(f"Checking file: {md_path}")

try:
    with open(md_path, 'rb') as f:
        content_bytes = f.read()

    # Try decoding as UTF-8
    content_str = content_bytes.decode('utf-8')
    print("\n--- CONTENT PREVIEW (UTF-8) ---")
    print(content_str[:500])
    
    # Check for specific mojibake characters
    if "婕旇" in content_str:
        print("\n[!] WARNING: Mojibake sequence found inside UTF-8 decoded string. The file content itself might be corrupted.")
    else:
        print("\n[OK] No common mojibake patterns detected in UTF-8 Text.")

except Exception as e:
    print(f"Error reading file: {e}")
