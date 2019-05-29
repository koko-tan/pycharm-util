import matplotlib.pyplot as plt
import matplotlib.colors as colors
import cv2 as cv
import numpy as np

im = cv.imread('/Users/tantaiyunfei/Desktop/图片/WechatIMG21.jpg')
im = cv.cvtColor(im, cv.COLOR_BGR2GRAY)

plt.imshow(im / im.max(axis=(0, 1)))
plt.colorbar()
plt.show()