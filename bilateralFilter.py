import cv2 as cv
import numpy as np


def I(im, i, j):
    return im[i, j]
image_path = '/Users/tantaiyunfei/Desktop/图片/WechatIMG73.jpeg'


im = cv.imread(image_path)
im = cv.resize(im, (600, 400))


def bilateralFilter(im, N, sigma_s, sigma_r):
    w, h = im.shape
    newIm = np.zeros([w+2*N, h+2*N], np.uint8)
    out = np.zeros([w+2*N, h+2*N], np.uint8)
    newIm[N:-N, N:-N] = im
    w, h = newIm.shape
    ws = np.zeros([2*N+1, 2*N+1])
    wr = np.zeros([2*N+1, 2*N+1])
    print(h)
    for x in range(N, w - N):
        for y in range(N, h - N):
            sum_fenzi = 0
            sum_fenmu = 0
            for i in range(x - N, x + N):
                for j in range(y - N, y + N):
                    ws = np.exp(((i-x)**2 + (j-y)**2) / (2*(sigma_s)**2))
                    wr = (newIm[i, j] - newIm[x, y])**2 / (2*(sigma_r)**2)
                    W = ws * wr
                    sum_fenmu += W
                    sum_fenzi += W*newIm[x, y]
            out[x, y] = sum_fenzi / sum_fenmu

    return out[N:w-N, N:h-N]


gray = cv.cvtColor(im, cv.COLOR_BGR2GRAY)
# print(gray)
im = bilateralFilter(gray, 7, 10, 10)
# print(im)
cv.imshow("高斯双边滤波结果", im)


cv.waitKey(0)
cv.destroyAllWindows()