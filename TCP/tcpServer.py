from socket import *


# 创建TCP监听套接字
tcpSocket = socket(AF_INET, SOCK_STREAM)
# 设置绑定的信息
localAddress = ('', 9000)
# 绑定端口
tcpSocket.bind(localAddress)
# 设置最大连接数
tcpSocket.listen(1)
# 设置服务关闭标志位
on = 1

# 开始监听
while True:
    try:
        print("——待接入——")
        connect, clientAddress = tcpSocket.accept()

        while True:
            try:
                data = connect.recv(1024).decode()

                if (not data) or (data == "bye"):  # 收到"bye"关闭当前连接
                    connect.close()
                    print("{} : {}    ————    连接关闭".format(clientAddress, data))
                    break

                elif data == "shut down":  # 收到"shut down"关闭服务器
                    tcpSocket.close()
                    on = 0
                    print("{} : {}    ————    服务关闭".format(clientAddress, data))
                    break

                else:
                    print("{} : {}".format(clientAddress, data))

                # 键入数据
                data = input("服务器发送 ： ")
                connect.send(data.encode())
                print("已发送")

            except:
                connect.close()

        if on == 0:
            break

    except:
        tcpSocket.close()
        break

