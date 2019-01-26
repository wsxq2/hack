#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
host = "www.baidu.com"
port = 80
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 创建socket
client.connect((host, port))  # 连接服务器
i = 0
client.send("GET / HTTP/1.1\r\n\r\n")  # 发送数据
while i < 100:
    response = client.recv(4096)  # 接收数据
    if not response:
        break
    print response
    i += 1
client.close()  # 关闭socket对象
