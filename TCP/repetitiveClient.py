#UDP回射服务器，客户端
from socket import *

#创建套接字
udpSocket = socket(AF_INET, SOCK_DGRAM)

#设置发送地址、端口
aimAddress = ('192.168.43.175', 8090)

while True:
    #后续函数接收bytes类型的串，此处需要转码
    data = input("键入需要传送的数据\n").encode()
    udpSocket.sendto(data, aimAddress)

udpSocket.close()