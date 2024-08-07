import socket
import sys

#TCP/IPソケットの作成
sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)

#ソケットの接続
server_address = './socket_file'
print(f"{server_address}に接続しています。")

#サーバへの接続を試みる
try:
    sock.connect(server_address)
except socket.error as err:
    print(err)
    sys.exit(1)

input = input("メッセージを入力してください。")
print(input)
if input != "name" and input != "address" and input != "mail" and input != "text":
    print("name address mail textからメッセージを選択し、入力してください。")
    sys.exit(1)

try:
    message = input.encode()
    sock.sendall(message)

    sock.settimeout(2)

    try:
        while True:
            data = str(sock.recv(256))

            if data:
                print("サーバの応答： " + data)
            else:
                break
    except(TimeoutError):
        print("ソケットがタイムアウトしました。サーバからの応答待ちを中止します")
finally:
    print("ソケットを閉じます。")
    sock.close()