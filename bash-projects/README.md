# Bash Projects 🐧

> Collection of Bash automation scripts for system administration, file management, and DevOps tasks.

---

## 📁 Scripts Overview

| Script | Description | Use Case |
|--------|-------------|----------|
| **FileSorter.sh** | Automated file organization by extension | Sorts files into folders based on their file extensions |

---

## 🚀 Quick Start

### Prerequisites
- Bash shell (version 3.0+)
- Basic Unix/Linux commands
- Appropriate file permissions

### Running Scripts

#### FileSorter.sh
Organizes files in a directory by creating folders based on file extensions and moving files accordingly.

```bash
# Make script executable
chmod +x FileSorter.sh

# Edit the BASE_FOLDER variable to your target directory
# Then run the script
./FileSorter.sh
```

**Features:**
- Handles special characters in filenames
- Case-insensitive extension sorting
- Creates folders automatically
- Safe error handling for missing directories

---

## 🛠️ Technologies Used

- **Bash** - Shell scripting
- **Unix utilities** - find, sort, tr, mkdir, mv
- **File system operations** - Directory traversal and file manipulation

---

## 📚 Learning Objectives

- ✅ Bash scripting fundamentals
- ✅ File system automation
- ✅ Error handling in shell scripts
- ✅ String manipulation and processing
- ✅ Safe file operations with special characters

---

## 🔧 Customization

To adapt scripts for your environment:
1. Update directory paths in script variables
2. Modify file extension handling logic as needed
3. Add additional error checking for your use case