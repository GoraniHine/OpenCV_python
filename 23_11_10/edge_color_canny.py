import cv2

def onTrackbar(th):
    edge = cv2.GaussianBlur(gray, (5, 5), 0)
    edge = cv2.Canny(edge, th, th*2, 5)

    color_edge = cv2.copyTo(image, mask = edge)
    dst = cv2.hconcat([image, color_edge])
    cv2.imshow("color edge", dst)

image = cv2.imread("ch7images/color_edge.jpg", cv2.IMREAD_COLOR)
if image is None: raise Exception("입력파일 읽기 오류")

th = 50
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
dst = cv2.hconcat([image, image])
cv2.imshow("color edge", dst)
cv2.createTrackbar("Canny th", "color edge", th, 150, onTrackbar)
onTrackbar(th)
cv2.waitKey(0)