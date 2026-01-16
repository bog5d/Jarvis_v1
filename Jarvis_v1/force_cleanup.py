import os
import shutil
import stat
import time

# ================= CONFIGURATION =================
SOURCE_TO_DELETE = r"C:\Users\王波\OneDrive\my_system\Inbox\Yarle_Output_Final"

def on_rm_error(func, path, exc_info):
    """
    错误回调函数：尝试修改文件权限并重试删除
    """
    try:
        # 尝试移除只读属性
        os.chmod(path, stat.S_IWRITE)
        # 再次尝试删除
        func(path)
        print(f"    [Retry Success] Deleted: {path}")
    except Exception as e:
        print(f"    [Retry Failed] Cannot delete {path}: {e}")

def main():
    print(f"Starting force cleanup of: {SOURCE_TO_DELETE}")
    
    if not os.path.exists(SOURCE_TO_DELETE):
        print("Path does not exist. Already clean?")
        return

    print("Deleting... This may take a moment.")
    
    try:
        # 使用 shutil.rmtree 配合错误处理回调
        shutil.rmtree(SOURCE_TO_DELETE, onerror=on_rm_error)
        print("✅ Cleanup Complete. Source folder removed.")
    except Exception as e:
        print(f"❌ Critical Error during cleanup: {e}")
        
    # Double check
    if os.path.exists(SOURCE_TO_DELETE):
        print("⚠️ Warning: Folder still exists (files might be locked by OneDrive sync engine).")
        print("Tip: pausing OneDrive sync might help.")
    else:
        print("🎉 Verify: Folder is gone. Space freed.")

if __name__ == "__main__":
    main()
