import os
import socket
import sys
from faker import Faker

def main():
    
    #TCP/IPソケットの作成
    sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)

    #ソケットの接続
    server_address = '/tmp/socket_file'
    print(f"{server_address}に接続しています。")

    #サーバへの接続を試みる
    try:
        socket.connect(server_address)
    except socket.error as err:
        print(err)
        sys.exit(1)
    
    input = inputMessage()



def inputMessage():
    message = input("メッセージを入力してください。")
    if message != "name" and message != "address" and message != "mail" and message != "text":
        print("name address mail textからメッセージを選択し、入力してください。")
        sys.exit(1)
    return message
