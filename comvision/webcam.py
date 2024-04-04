import cv2
from pathlib import Path

WEB_CAM_IDX = 0
cam = cv2.VideoCapture(WEB_CAM_IDX)

while cam.isOpened():
    status, frame = cam.read()
    if not status:
        break
    cv2.imshow('Webcam', frame)
    if cv2.waitKey(1) == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()