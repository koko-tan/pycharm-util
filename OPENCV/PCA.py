import numpy as np
import cv2 as cv


def PCA_Image(image, N=5):
    for i in range(3):
        u, sigma, v = np.linalg.svd(image[:, :, i])

        u = u[:, 0:N]
        temp = np.zeros([N, N])
        for j in range(N):
            temp[j, j] = sigma[j]

        sigma = temp
        v = v[0:N, :]

        image[:, :, i] = np.dot(np.dot(u, sigma), v)

def PCA(image, N=5):
    temp = []
    image = image.astype(float)

    for i in range(3):
        image[:, :, i] -= np.mean(image[:, :, i])
        COV = np.dot(image[:, :, i].T, image[:, :, i]) / image[:, :, i].shape[0]

        U, S, V = np.linalg.svd(COV)

        image[:, :, i] = np.dot(image[:, :, i], U)





im = cv.imread("/Users/tantaiyunfei/Desktop/图片/IMG_4394副本.jpg")

rate = 8
w, h, ch = im.shape
im = cv.resize(im, (int(h / rate), int(w / rate)))
PCA(im, 100)
cv.namedWindow("result", cv.WINDOW_AUTOSIZE)
cv.imshow("result", im)


# print(np.zeros(im.shape))
c = cv.waitKey(0)
if c == 27:
    cv.destroyAllWindows()


