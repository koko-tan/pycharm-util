import cv2 as cv

imagePath = '/Users/tantaiyunfei/Desktop/图片/IMG_4196.jpg'

rate = 8

im = cv.imread(imagePath)

w, h, ch = im.shape

im = cv.resize(im, (int(h/rate), int(w/rate)))


cv.imshow("原图", im)

guassIm = cv.GaussianBlur(im, (0, 0), 1.7)

cannyIm = cv.Canny(guassIm, 50, 150)


cv.imshow("processed", cannyIm)


cv.waitKey(0)
cv.destroyAllWindows()