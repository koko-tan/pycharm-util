# 简单的UDP回射服务器
from socket import *

#创建套接字
udpSocket = socket(AF_INET, SOCK_DGRAM)

#绑定本地接收端口
localAddress = ('', 8090)
udpSocket.bind(localAddress)

#定义回射端口
aimPort = 9000

while True:
    recvData = udpSocket.recvfrom(1024)
    aimAddress = (recvData[1][0], aimPort)

    udpSocket.sendto(recvData[0], aimAddress)

    print("Message passed --- {} : {}".format(recvData[0], aimAddress))

udpSocket.close()