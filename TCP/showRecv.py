#用来显示收到的数据
from socket import *

#创建套接字
udpSocket = socket(AF_INET, SOCK_DGRAM)

#绑定本地接收端口
bindAddress = ('', 9000)
udpSocket.bind(bindAddress)

while True:
    rec = udpSocket.recvfrom(1024)
    print("Data : {} | from : {}".format(rec[0].decode(), rec[1]))

udpSocket.close()