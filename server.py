import socket

def xor_encrypt(data, key):
    encrypted_data = bytearray()
    for byte in data:
        encrypted_data.append(byte ^ key)
    return encrypted_data

def receive_file(server_socket, filename, key):
    with open(filename, 'wb') as file:
        while True:
            data = server_socket.recv(1024)
            if not data:
                break
            decrypted_data = xor_encrypt(data, key)
            file.write(decrypted_data)

def main():
    host = '0.0.0.0'
    port = 12345
    key = 0xAA  # XOR encryption key
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)
    print(f"Server listening on {host}:{port}")
    client_socket, client_addr = server_socket.accept()
    print(f"Connection from {client_addr[0]}:{client_addr[1]}")
    filename = 'received_file.txt'
    receive_file(client_socket, filename, key)
    client_socket.close()
    server_socket.close()
    print(f"File '{filename}' received and saved.")

if __name__ == '__main__':
    main()
