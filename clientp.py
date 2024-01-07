import socket
from cryptography.fernet import Fernet

def xor_encrypt(data, key):
    encrypted_data = bytearray()
    for byte in data:
        encrypted_data.append(byte ^ key)
    return encrypted_data


def generate_key():
    key = Fernet.generate_key()
    return key


def encrypt_file(key, input_file):
    fernet = Fernet(key)
    with open(input_file, 'rb') as file:
        file_data = file.read()
    encrypted_data = fernet.encrypt(file_data)
    with open(input_file, 'wb') as file:
        file.write(encrypted_data)


def send_file(client_socket, filename, key):
    with open(filename, 'rb') as file:
        data = file.read(1024)
        while data:
            encrypted_data = xor_encrypt(data, key)
            client_socket.send(encrypted_data)
            data = file.read(1024)

def main():
    host = '127.0.0.1'
    port = 12345
    key = 0xAA  # XOR encryption key
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))
    filename = 'transfer.txt'
    key1=str(generate_key())
    key1=key1[2:len(key1)-1]
    encrypt_file(key1,filename)
    send_file(client_socket, filename, key)
    client_socket.close()
    print(f"File '{filename}' sent to the server.")
    print(key1)

if __name__ == '__main__':
    main()
