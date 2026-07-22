from pathlib import Path 
from datetime import datetime
folder = input("Enter folder name: ") 
folder = Path(folder)
file_count = 0
directory_count = 0
total = 0
if folder.is_dir(): 
   print("Folder exists.")
   print("Name: ", folder.name)
   print("Parent Folder: ", folder.parent)
   print("Absolute Path: ", folder.resolve())
   print("Current working directory: ", Path.cwd())
   print("\nContents:")
   print("\nDirectories:")
   items = list(folder.rglob("*"))
   for item in items:
      if item.is_dir():
         info = item.stat()
         modified = datetime.fromtimestamp(info.st_mtime)
         print(item)
         print(f"Modified: {modified.strftime("%Y-%m-%d %A %H-%M-%S")}")
         directory_count += 1
   print("\nFiles:")
   for item in items:
      if item.is_file():
         info = item.stat()
         modified = datetime.fromtimestamp(info.st_mtime)
         print(item)
         print(f"Size: {info.st_size} bytes")
         print(f"Modified: {modified.strftime("%Y-%m-%d %A %H-%M-%S")}")
         file_count += 1
   total = file_count + directory_count
   print("\nStatistics:")
   print(f"Directories: {directory_count}")
   print(f"Files: {file_count}")
   print(f"Total items: {total}")
else:
   print(f"Folder {folder} does not exist.")