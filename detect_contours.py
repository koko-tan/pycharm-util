import cv2

path = '/Users/tantaiyunfei/Desktop/图片/IMG_1773.jpg'
img = cv2.imread(path)
w, h, ch = img.shape
rate = 6
img = cv2.resize(img, (int(h/rate), int(w/rate)))
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY|cv2.THRESH_OTSU)

_, contours, hierarchy = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(img, contours, -1, (0, 0, 255), 2)

cv2.imshow("img", img)
cv2.waitKey(0)

cv2.approxPolyDP()