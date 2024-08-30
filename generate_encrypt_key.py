from cryptography.fernet import Fernet

def generate_key(file_path):
    # Generate a key
    key = Fernet.generate_key()
    
    # Write the key to a file
    with open(file_path, 'wb') as key_file:
        key_file.write(key)
    
    print(f"Encryption key generated and saved to {file_path}")

if __name__ == "__main__":
    # Path to save the key file
    key_file_path = "encryption_key.txt"
    
    # Generate and store the key
    generate_key(key_file_path)
