import os
import shutil

path = "moved/copied_text.txt"
dir_path = "moved"

try:
    os.remove(path)
except FileNotFoundError:
    print("File not found")
except PermissionError:
    print("Permission denied")
else:
    print("File deleted")

try:
    os.rmdir(dir_path)
except FileNotFoundError:
    print("File not found")
except PermissionError:
    print("Permission denied")
except OSError:
    print("Cannot delete using rmdir")
    print("Use function shutil.rmtree(path) to remove the folder")
else:
    print("Folder deleted")