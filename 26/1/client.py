from socket import *
import struct

client = socket(AF_INET, SOCK_STREAM)
client.connect(('localhost', 8080))  # 拨电话，地址为服务端的ip和端口
while True:
    cmd = input('>>>：').strip()
    if not cmd:
        continue
    client.send(cmd.encode('utf-8'))
    # 接收自定义报头
    res = client.recv(4)
    header = struct.unpack('i', res)[0]
    # 根据传过来的数据长度，来接收数据
    data_size = 0
    total_data = b''
    while data_size < header:
        data_recv = client.recv(512)
        total_data += data_recv
        data_size += len(data_recv)

    print(total_data.decode('gbk'))
client.close()
