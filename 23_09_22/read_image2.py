import cv2
from Common.utils import print_matInfo

title1, title2 = 'gray2gray', 'gray2color'
gray2gray = cv2.imread("sample/ch4/images/read_gray.jpg", cv2.IMREAD_GRAYSCALE)
gray2color = cv2.imread("sample/ch4/images/read_gray.jpg", cv2.IMREAD_COLOR)

if gray2gray is None or gray2color is None:
    raise Exception("영상파일 읽기 에러")

print("행렬 좌표 (100, 100) 화소값")
print("%s %s" % (title1, gray2gray[100, 100]))
print("%s %s\n" % (title2, gray2color[100, 100]))

print_matInfo(title1, gray2gray)
print_matInfo(title2, gray2color)

cv2.imshow(title1, gray2gray)
cv2.imshow(title2, gray2color)
cv2.waitKey(0)