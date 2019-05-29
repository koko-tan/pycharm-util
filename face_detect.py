import cv2 as cv

# 人脸检测
def image_faceDetect(image):
    # 转换成灰度图像
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    # 载入模型
    modePath = '/Users/tantaiyunfei/Desktop/——环境——/opencv人脸检测模型/haarcascade_frontalface_alt_tree.xml'
    # 获得检测器
    detector = cv.CascadeClassifier(modePath)
    # 人脸检测
    face = detector.detectMultiScale(gray, 1.8, 1)

    # 将检测到的人脸信息框，绘制到原图
    for i in face:
        x, y, w, h = i
        cv.rectangle(image, (x, y), (x+w, y+h), (0, 0, 255), 2)
    # 显示
    cv.imshow("result", image)


# 摄像头信息获取与图像显示
def video_faceDetect():
    # 获取摄像头
    capture = cv.VideoCapture(0)

    while True:
        # 读取摄像头图像
        ret, frame = capture.read()
        # 反转图像
        frame = cv.flip(frame, 1)
        # 缩放图像
        frame = resize(frame)
        # 人脸检测
        image_faceDetect(frame)
        # 窗口显示
        c = cv.waitKey(10)

        # Esc退出
        if c == 27:
            break


# 缩放函数
def resize(image, rate = 2):
    w, h, _ = image.shape
    w = round(w / rate)
    h = round(h / rate)
    return cv.resize(image, (h, w))

# 主函数
def main():
    video_faceDetect()


if __name__ == "__main__":
    main()