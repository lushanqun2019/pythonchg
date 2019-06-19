from socket import *
import subprocess
import struct

server = socket(AF_INET, SOCK_STREAM)  # 买电话
server.bind(('localhost', 8080))  # 插手机卡，补充：0-65535 0-1024给系统用的
server.listen(5)  # 进入待机状态，5指的是挂起连接数，就是backlog，指的是同一时间可以来五个请求

while True:
    conn, client_address = server.accept()  # 等电话连接
    print(client_address)
    while True:     # 连接循环
        try:
            cmd = conn.recv(512)
            obj = subprocess.Popen(cmd.decode('gbk'),
                                   shell=True,
                                   stdout=subprocess.PIPE,
                                   stderr=subprocess.PIPE
                                   )
            stdout = obj.stdout.read()
            stderr = obj.stderr.read()
            # 发送自定义报头
            header = struct.pack('i', len(stdout) + len(stderr))
            # 发送报头和数据
            conn.send(header)
            conn.send(stdout)
            conn.send(stderr)
        except ConnectionResetError:
            break
    # 关闭链接
    conn.close()
# 关闭服务器
server.close()
