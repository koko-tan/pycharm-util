import cv2
import matplotlib.pyplot as plt
import numpy as np


# 主函数
def main():
    # 设置图像路径
    imagePath = "/Users/tantaiyunfei/Desktop/图片/背景图/3a78554539925d8104b3054e0270ddb7.jpg"

    # 读取图像
    image = plt.imread(imagePath)
    image = image.astype(float)

    for i in range(image.shape[2]):

        image[:, :, i] -= np.mean(image[:, :, i])

        cov = np.dot(image[:, :, i].T, image[:, :, i])

        U, D, V = np.linalg.svd(cov)

        image

    plt.imshow(image)
    plt.show()







if __name__ == "__main__":
    main()

