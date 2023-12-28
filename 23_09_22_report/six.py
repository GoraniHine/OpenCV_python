import numpy as np, cv2

image = np.zeros((300, 400), np.uint8)
image[:] = 100

title = 'window'
cv2.namedWindow(title, cv2.WINDOW_AUTOSIZE)
cv2.moveWindow(title, 100, 200)
cv2.imshow(title, image)
cv2.resizeWindow(title, 500, 600)

cv2.waitKey(0)
cv2.destroyAllWindows()