# Project 02 - File Integrity Checker

## Description

File Integrity Checker is a Python-based cybersecurity tool that monitors the integrity of files inside a directory.

The program scans all files, calculates their SHA-256 hashes, stores them in a JSON database, and compares the current scan with previous results.

It can detect:

- New files
- Modified files
- Deleted files
- Unchanged files

This project was created as part of my Cybersecurity Projects learning journey.

---

## Features

- Scan files recursively using pathlib
- Calculate SHA-256 hashes with hashlib
- Store hashes in a JSON database
- Detect modified, deleted, new, and unchanged files
- Command Line Interface (CLI) using argparse
- Logging system using the logging module
- Error handling with try/except
- Efficient hashing using chunk-based file reading

---

## Technologies Used

- Python 3
- pathlib
- hashlib
- json
- logging
- argparse

---

## Project Structure

```
Project-02-File-Integrity-Checker/
│
├── main.py
├── database.json
└── README.md
```

---

## Usage

Clone the repository and run:

```bash
python main.py <folder>
```

Example:

```bash
python main.py TestFolder
```

or

```bash
python main.py ..
```

---

## Example Output

```
Folder found.

UNCHANGED: notes.txt
MODIFIED: config.json
NEW: passwords.txt
DELETED: old_backup.txt

Summary
-------
UNCHANGED: 12
MODIFIED: 1
NEW: 2
DELETED: 1
```

---

## Skills Practiced

This project helped me practice:

- File system navigation
- Recursive directory scanning
- Cryptographic hashing
- JSON serialization
- Command Line Interface (CLI)
- Logging
- Exception handling
- Writing reusable functions
- Git & GitHub workflow

---

## Future Improvements

- Support multiple hashing algorithms (SHA-1, SHA-512, MD5)
- Ignore selected files or directories
- Export scan reports
- Colorized terminal output
- Configuration file support
- Automatic scheduled scanning
- Multi-threaded scanning for better performance

---

## Author

Rahim Shirinov

Cybersecurity Learning Project