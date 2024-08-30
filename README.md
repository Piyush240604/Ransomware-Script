# **Ransomware Demonstration Script**

This repository contains two Python scripts for a simple ransomware demonstration. **Disclaimer**: This is intended solely for educational purposes. Do not use this code maliciously or in real-world scenarios.

## **Files**

- **`generate_encryption_key.py`**: This script generates an encryption key and saves it to a file named `encryption_key.txt`.
- **`ransomware.py`**: This script monitors the `<Your Specified Target>` folder for any new files. When a new file is detected, it encrypts the file using the previously generated encryption key and displays a popup message.

## **How It Works**

### **1. `generate_encryption_key.py`**

This script:
- Generates a 16-byte encryption key using Python's `cryptography` library.
- Saves the key in a file named `encryption_key.txt` located in the same directory as the script.

### **2. `ransomware.py`**

This script:
- Monitors the `Downloads` folder for any newly added files.
- Encrypts the newly added files using the encryption key stored in `encryption_key.txt`.
- Displays a popup message informing the user that their files have been encrypted.
- Runs silently in the background without displaying a terminal window if set up using `pythonw.exe`.

## **Setup and Installation**

### **1. Clone the Repository**

```bash
git clone https://github.com/yourusername/ransomware-demo.git
cd ransomware-demo
```

### **2. Set Up a Virtual Environment**

```bash
python -m venv renv
source renv/bin/activate  # On Windows use `renv\Scripts\activate`
```

### **3. Install Dependencies**

```bash
pip install -r requirements.txt
```

### **4. Generate the Encryption Key**

```bash
python generate_encryption_key.py
```

### **5. Run the Ransomware Script**

```bash
pythonw ransomware.py  # Runs without showing the terminal window
```

## **Running on System Startup**

To run the `ransomware.py` script automatically on system startup without displaying a terminal window:

### **1. Using Task Scheduler (Windows)**

1. Open **Task Scheduler** and create a new task.
2. Set the task to run **at startup** and point to the `ransomware.py` script using `pythonw.exe`:
   ```bash
   "path\to\pythonw.exe" "path\to\ransomware.py"
   ```

### **2. Using Windows Registry**

1. Open **Registry Editor** (`regedit`) and navigate to:
   ```bash
   HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Run
   ```
2. Add a new string value with the command:
   ```bash
   "path\to\pythonw.exe" "path\to\ransomware.py"
   ```

## **Logging**

The script outputs any errors or logs to `log.txt` located in the same directory as `ransomware.py`.

## **Disclaimer**

This code is intended for educational purposes only. Running this code in a production environment or using it maliciously is illegal and unethical.

## **License**

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
