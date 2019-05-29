from socket import *


# 创建套接字
tcpSocket = socket(AF_INET, SOCK_STREAM)

# 设置目标服务器地址信息
aimAddress = ('192.168.43.175', 9000)

# 绑定本地端口
tcpSocket.connect(aimAddress)
print("——连接成功——")

while True:
    try:
        # 键入数据
        data = input("本机发送 ： ")
        # 发送数据
        tcpSocket.send(data.encode())
        print("已发送")
        # 接收数据
        data = tcpSocket.recv(1024).decode()
        print(data)

        if not data:
            tcpSocket.close()
            print("——客户端关闭——")
            break
        elif data == "bye":
            tcpSocket.close()
            print("——发起关闭连接请求并关闭客户端——")

    except:
        tcpSocket.close()
        print("——客户端异常关闭——")
        break