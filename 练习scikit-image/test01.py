import matplotlib.pyplot as plt
import cv2
from skimage import feature
from skimage import data
import numpy as np

def returnResizeImage(path, rate):
    im = cv2.imread(path)
    h, w = im.shape[:2]
    im = cv2.resize(im, (int(w / rate), int(h / rate)))
    return cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)


path1 = '/Users/tantaiyunfei/Desktop/图片/IMG_4404.jpg'
path2 = '/Users/tantaiyunfei/Desktop/图片/IMG_4405.jpg'
rate = 8
im1 = returnResizeImage(path1, rate)
im2 = returnResizeImage(path2, rate)

orb = cv2.ORB_create(2000)
kp1, des1 = orb.detectAndCompute(im1, None)
kp2, des2 = orb.detectAndCompute(im2, None)
bf = cv2.BFMatcher()
matches = bf.knnMatch(des1,des2, k=2)
good = []
for m,n in matches:
    if m.distance < 0.5*n.distance:
        good.append([m])
img5 = cv2.drawMatchesKnn(im1,kp1,im2,kp2,good,None,flags=2)
cv2.imshow("ORB", img5)
c = cv2.waitKey(0)
if c == 27:
    cv2.destroyAllWindows()