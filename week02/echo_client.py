# -*- coding: utf-8 -*-
import os
import socket
import sys

HOST = 'localhost'
PORT = 10100


def echo_client():
    file_path = input('input > ')

    # 判断上传文件是否存在
    if not os.path.isfile(file_path):
        print("该文件不存在")
        sys.exit()
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))

    # 获取到文件名
    file_name = os.path.basename(file_path)

    # filename + 文件名 发送给服务端进行正则匹配处理
    file_name = file_name.strip()

    # 发送文件名
    s.sendall(file_name.encode())

    # 传输文件
    with open(file_path, "rb") as f:
        data = f.read()
        s.sendall(data)
    s.close()


if __name__ == '__main__':
    echo_client()
