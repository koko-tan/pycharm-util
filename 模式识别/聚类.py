# 程序用到了`opencv`、`matplotlib`和`numpy`库，请先自行配置。
# 第`11`行换成要处理图像的路径

import cv2
import matplotlib.pyplot as plt
import numpy as np


# ======准备工作======
# 原图像路径
imPath = 'xxx.jpg'

# 读取图像
origin = cv2.imread(imPath)

# 将图像转换为灰度图像
origin = cv2.cvtColor(origin, cv2.COLOR_BGR2GRAY)

# 图像大小信息
h, w = origin.shape
print("原始图像大小为 ：{}*{}".format(h, w))

# 设置缩放系数，系数越大缩放程度越强
alpha = int(input("\n请输入缩放系数 ： "))

# 图像缩放
newH = int(h / alpha)
newW = int(w / alpha)
print("\n缩放后图像大小 : {}*{}".format(newH, newW))
origin = cv2.resize(origin, (newW, newH))

# 设置分为几类
numOfClass = int(input("\n色彩分类数 ： "))

# 设置最大迭代次数
roundForLoop = int(input("\n定义最大迭代次数 ： "))
print()

# ======进行聚类======
print("————开始聚类————")

# 以等分最大与最小区间来初始化numOfClass个中心点
valueArange = origin.max() - origin.min()
keyValueList = []  # 用来存储numOfClass个中心点的值

for i in range(1, numOfClass + 1):
    keyValueList.append(valueArange / numOfClass * i / 2)

# 聚类更新keyValueList
flagMatrix = np.zeros((newH, newW))

for r in range(roundForLoop):

    for row in range(newH):

        for col in range(newW):

            temp = []

            for i in range(numOfClass):
                temp.append(np.abs(origin[row, col] - keyValueList[i]))

            # 获得该像素点最近的类
            index = temp.index(min(temp))
            # 存入flag矩阵
            flagMatrix[row, col] = index

    # 更新keyValueList
    temp = np.zeros(numOfClass)
    ct = np.zeros(numOfClass)

    for row in range(newH):

        for col in range(newW):
            temp[int(flagMatrix[row, col])] += origin[row, col]
            ct[int(flagMatrix[row, col])] += 1

    for i in range(numOfClass):
        keyValueList[i] = temp[i] / ct[i]

    print("完成 ： {} / {}".format(r + 1, roundForLoop))

# 显示缩放后的待处理图像
plt.subplot(121)
plt.imshow(origin)
plt.title("Origin Image")

# 显示聚类结果
plt.subplot(122)
plt.imshow(flagMatrix)
plt.title("Result1 Image\nRound = {}\nclass = {}".format(roundForLoop, numOfClass))
plt.show()