import os

file_path = r"D:\My_System\Inbox\Enex_Flat\01_每日收集组__EverMemo.enex"

def check_encoding(path):
    try:
        with open(path, 'rb') as f:
            raw = f.read(1000)
        return raw
    except Exception as e:
        return str(e)

raw_bytes = check_encoding(file_path)
print(f"First 100 bytes: {raw_bytes[:100]}")
try:
    print(f"Decoded UTF-8: {raw_bytes.decode('utf-8')[:100]}")
except:
    print("UTF-8 Decode Failed")

try:
    print(f"Decoded GBK: {raw_bytes.decode('gbk')[:100]}")
except:
    print("GBK Decode Failed")
