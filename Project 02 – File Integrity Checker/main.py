import hashlib
from pathlib import Path
import json
import logging
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("folder")
args = parser.parse_args()
folder = Path(args.folder)
json_file = Path("database.json")
database = {}
CHUNK_SIZE = 4096
logging.basicConfig(
    filename = "scan.log",
    level = logging.INFO,
    format = "%(asctime)s | %(levelname)s | %(message)s"
)
unchanged_count = 0
modified_count = 0
new_count = 0
logging.info("Scan started.")
def calculate_sha256(file): 
    sha = hashlib.sha256()
    print(f"File {file} exists!")
    with file.open("rb") as f:
        while True:
            chunk = f.read(CHUNK_SIZE)
            if not chunk:
                break
            sha.update(chunk)
    return sha.hexdigest()
if folder.is_dir():
    logging.info(f"Folder found: {folder}")
    print(f"Folder {folder} exists!")
    items = list(folder.rglob("*"))
    old_database = {}
    new_files = []
    if json_file.exists():
        try:
            with json_file.open("r") as f:
                old_database = json.load(f)
        except json.JSONDecodeError:
            logging.error("Database is corrupted.")
            print("Database is corrupted.\nCreating a new database...")
        except PermissionError:
            logging.error("Permission denied")
            print("Permission denied.")
        except Exception as error:
            logging.error(f"Unexpected error: {error}")
            print(error)
    for item in items:
        if item.is_file():
                logging.debug(f"Scanning file: {item}")
                sha256 = calculate_sha256(item)
                print(f"\nFile: {item.name}")
                print(f"SHA256: {sha256}")
                if str(item) in old_database:
                    old_sha256 = old_database[str(item)]
                    if old_sha256 == sha256:
                        logging.debug(f"Unchanged file: {item}")
                        unchanged_count += 1
                        print(f"UNCHANGED: {item}")
                    else:
                        logging.warning(f"Modified file: {item}")
                        modified_count += 1
                        print(f"MODIFIED: {item}")
                else:
                    logging.info(f"New file: {item}")
                    new_count += 1
                    new_files.append(item)
                database[str(item)] = sha256
    deleted_files = []
    for old_file in old_database.keys():
        if old_file not in database:
            logging.warning(f"Deleted file: {old_file}")
            deleted_files.append(old_file)
    for file in deleted_files:
        print(f"Deleted File: {file}")
    for file in new_files:
        print(f"New file: {file}")
    print(f"UNCHANGED: {unchanged_count}")
    print(f"MODIFIED: {modified_count}")
    print(f"NEW: {new_count}")
    print(f"DELETED: {len(deleted_files)}")
    with open("database.json", "w") as file:
        json.dump(database, file, indent = 4)
    logging.info("Scan finished")
else:
    logging.warning(f"Folder not found: {folder}")
    print(f"Folder {folder} doesn't exist")