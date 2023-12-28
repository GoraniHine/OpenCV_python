import numpy as np
import cv2

image = np.zeros((600, 400, 3), np.uint8)
image[:] = 255
title1= 'win mode1'

cv2. rectangle(image, (100, 100, 200, 300), (0, 0, 255), cv2.FILLED)

cv2.namedWindow(title1, cv2.WINDOW_AUTOSIZE)
cv2.moveWindow(title1, 0, 0)
cv2.imshow(title1, image)

cv2.waitKey(0)
cv2.destroyAllWindows()