import cv2

def onTrackbar(th1):
    th1 = cv2.getTrackbarPos("th1", "canny_edge")
    th2 = cv2.getTrackbarPos("th2", "canny_edge")
    edge = cv2.Canny(image, th1, th2)

    cv2.imshow("canny_edge", edge)

image = cv2.imread("ch7images/cannay_tset.jpg", cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("입력파일 읽기 오류")

th1, th2 = 50, 50
cv2.imshow("canny_edge", image)
cv2.createTrackbar("th1", "canny_edge", 0, 255, onTrackbar)
cv2.createTrackbar("th2", "canny_edge", 100, 255, onTrackbar)
onTrackbar(th1)
cv2.waitKey(0)