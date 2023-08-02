import os
from cryptography.fernet import Fernet

def load_key(file_path):
    with open(file_path, "rb") as key_file:
        return key_file.read()

def decrypt_file(file_path, symmetric_key):
    with open(file_path, "rb") as encrypted_file:
        encrypted_data = encrypted_file.read()

    fernet = Fernet(symmetric_key)
    decrypted_data = fernet.decrypt(encrypted_data)

    decrypted_file_path = file_path[:-len(".ransomwaretroll")]
    with open(decrypted_file_path, "wb") as decrypted_file:
        decrypted_file.write(decrypted_data)

def decrypt_folder(folder_path, symmetric_key):
    for root, dirs, files in os.walk(folder_path):
        for file_name in files:
            if file_name.endswith(".ransomwaretroll"):
                file_path = os.path.join(root, file_name)
                decrypt_file(file_path, symmetric_key)
                os.remove(file_path)

if __name__ == "__main__":

    folder_to_encrypt = "CAMINHO DO DIRETORIO - Failed"  # caminho da pasta que deseja descriptografar
    key_file_path = "symmetric_key.txt"

    symmetric_key = load_key(key_file_path)

    decrypt_folder(folder_to_encrypt, symmetric_key)

print("\n")
print("=========================================\n")
print("Todos os arquivos foram descriptografados\n")
print("=========================================\n")