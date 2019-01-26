#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
host = "kali"
port = 9999
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 创建socket
client.connect((host, port))  # 连接服务器
i = 0
while True:
    client.send("Hello Socket！")  # 发送数据
    response = client.recv(4096)  # 接收数据
    print response
    i += 1
client.close()  # 关闭socket对象
