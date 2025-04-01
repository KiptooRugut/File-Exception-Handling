# File Handling and Exception Handling Project

A Python program that reads a file, converts its content to uppercase, and saves a modified version to a new directory with proper error handling.

## Features

- File Reading: Safely reads text files with error handling for:
  - Non-existent files (`FileNotFoundError`)
  - Permission errors (`PermissionError`)
  - Directory inputs (`IsADirectoryError`)
  
- Content Modification: Converts all text to uppercase
  
- Directory Management:
  - Automatically creates `assets/modified` directory if it doesn't exist
  - Handles directory creation errors
  
- File Writing:
  - Creates new files with `_modified` suffix
  - Handles write permissions and other write errors

## Requirements

- Python 3

## Installation

1. Clone the repository:
```bash
git clone https://github.com/KiptooRugut/File-Exception-Handling.git

2. Navigate to project directory:
cd File-Exception-Handling

3. Run the script:
python3 File-exception-handling.py

4. When prompted, enter the path to your input file:
Enter the filename to read: assets/data/example.txt
