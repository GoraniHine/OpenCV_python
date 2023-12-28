import numpy as np, cv2

image = cv2.imread("ch8_images/contrast.jpg", cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("영상파일 읽기 에러")

h, w = image.shape

flip1 = np.array([[-1, 0, w], [0, 1, 0]], np.float32)
flip2 = np.array([[1, 0, 0], [0, -1, h]], np.float32)
flip3 = np.array([[-1, 0, w], [0, -1, h]], np.float32)

dst1 = cv2.warpAffine(image, flip1, (w, h))
dst2 = cv2.warpAffine(image, flip2, (w, h))
dst3 = cv2.warpAffine(image, flip3, (w, h))

cv2.imshow('image', image); cv2.imshow('flip1', dst1)
cv2.imshow('flip2', dst2); cv2.imshow('flip3', dst3)
cv2.waitKey()