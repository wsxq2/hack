#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
ip = "0.0.0.0"  # 监听IP地址0.0.0.0，在所有IP上面都绑定，在每个IP上都收到请求。
port = 9999  # 设置服务器监听的端口
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 创建一个服务用的socket
server.bind((ip, port))  # 绑定套接字的IP地址和端口地址
server.listen(1)  # 开启监听，设置数量
while True:  # 死循环，收发信息
    client, addr = server.accept()
    while True:
        request = client.recv(1024)
        if not request:
            break
        print addr, ": ", request
        client.send("Hello client!")  # 给客户端返回（发送）数据包
    client.close()  # 关闭
