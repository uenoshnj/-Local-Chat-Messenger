import socket
import os
from faker import Faker

fake = Faker('jp-JP')

sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)

server_address = "./socket_file"

try:
    os.unlink(server_address)

except FileNotFoundError:
    pass

print(f"起動しています {server_address}")

sock.bind(server_address)

sock.listen(1)

while True:
    connection, client_address = sock.accept()
    try:
        print("接続されました", client_address)

        while True:
            data = connection.recv(16)

            data_str = data.decode('utf-8')

            print("受領データ: " + data_str)

            if data:
                if data_str == "name":
                    response = fake.name()
                elif data_str == "address":
                    response = fake.address()
                elif data_str == "mail":
                    response = fake.providers.internet()
                elif data_str == "text":
                    response = fake.text
                
                connection.sendall(response.encode())
            else:
                print("データはありません。", client_address)
                break
    finally:
        print("接続を終了します。")
        connection.close()
