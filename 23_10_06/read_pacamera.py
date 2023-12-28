import cv2

def put_string(frame, text, pt, value, color=(120, 200, 90)):
    text += str(value)
    shade = (pt[0] + 2, pt[1] + 2)
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(frame, text, shade, font, 0.7, (0, 0, 0), 2)
    cv2.putText(frame, text, pt, font, 0.7, color, 2)

capture = cv2.VideoCapture("sample/ch4/images/test.mp4")
if capture.isOpened() == False:
    raise Exception("카메라 연결 안됨")

print("너비 %d" % capture.get(cv2.CAP_PROP_FRAME_WIDTH))
print("높이 %d" % capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
print("노출 %d" % capture.get(cv2.CAP_PROP_EXPOSURE))
print("밝기 %d" % capture.get(cv2.CAP_PROP_BRIGHTNESS))

while True:
    ret, frame = capture.read()
    if not ret: break
    if cv2.waitKey(30) >= 0:break

    exposure = capture.get(cv2.CAP_PROP_EXPOSURE)
    HEIGHT = capture.get(cv2.CAP_PROP_FRAME_HEIGHT)
    put_string(frame, 'EXPOS: ', (10, 40), exposure)
    put_string(frame, 'HEIGHT: ', (10, 80), HEIGHT)
    title = "View Frame from Camera"
    cv2.imshow(title, frame)

capture.release()
