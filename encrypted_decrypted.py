from cryptography.fernet import Fernet

def generate_key():
    key = Fernet.generate_key()
    return key




def encrypt_file(key, input_file, output_file):
    fernet = Fernet(key)
    with open(input_file, 'rb') as file:
        file_data = file.read()
    encrypted_data = fernet.encrypt(file_data)
    with open(output_file, 'wb') as file:
        file.write(encrypted_data)


def decrypt_file(key, input_file, output_file):
    fernet = Fernet(key)
    with open(input_file, 'rb') as file:
        encrypted_data = file.read()
    decrypted_data = fernet.decrypt(encrypted_data)
    with open(output_file, 'wb') as file:
        file.write(decrypted_data)




print("Please enter the Type of operation to perform\n1.Encryption\n2.Decryption")
n=int(input())
if n==1:
    print("Please enter the file name with path for Encryption")
    a = input()
    key=str(generate_key())
    key=key[2:len(key)-1]
    encrypt_file(key,a,a)
    print("Key %s"%key)
    print(f'File {a} is  encrypted and saved.')
elif n==2:
    print("Please enter the file name with path for Decryption")
    file=input()
    print("Please enter the Key to decrypt")
    key=input()
    decrypt_file(key, file, file)
    print(f'File {file} decrypted and saved.')