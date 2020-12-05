import socket
import re
import sys

HOST = 'localhost'
PORT = 10100


def echo_server():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 对象s绑定到指定的主机和端口上
    s.bind((HOST, PORT))
    # 只接受1个连接
    s.listen(1)

    while True:
        # accept表示接受用户端的连接
        conn, addr = s.accept()
        # 输出客户端地址
        print(f'Connected by {addr}')
        file = conn.recv(1024)

        # 接收到字符转码
        file = file.decode()

        # 接收到文件写入文件
        with open("new" + file, "wb") as f:
            while True:
                data = conn.recv(10240)
                if not data:
                    break
                f.write(data)
        f.close()
        print(f"文件 {file} 传输已完成。")
        conn.close()


if __name__ == '__main__':
    echo_server()
