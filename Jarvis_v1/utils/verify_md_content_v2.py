import os
import glob

# Search recursively for any MD file in the notes directory
search_path = r"C:\Users\王波\OneDrive\my_system\inbox\Yarle_Output_Pilot_V4\notes\**\*.md"
files = glob.glob(search_path, recursive=True)

if not files:
    print("No MD file found.")
    exit()

md_path = files[0]
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
