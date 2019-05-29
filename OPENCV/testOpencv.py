import cv2
import numpy as np


imPath = '/Users/tantaiyunfei/Desktop/图片/IMG_1845.jpg'
im = cv2.imread(imPath,)
w, h, ch = im.shape

gray= cv2.resize(gray, (689, 965))
gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
cv2.imshow("origin", gray)
im = cv2.bilateralFilter(gray, 0, 150, 30)
cv2.imshow("processed", gray)

cv2.imshow("bilateraled", im)
cv2.imshow("result", cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 5, 5))
cv2.waitKey(0)
cv2.destroyAllWindows()


