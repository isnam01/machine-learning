#!/usr/bin/python
import cv2
cap=cv2.VideoCapture(0)
while cap.isOpened():
    status,frame=cap.read()
    redimg=cv2.inRange(frame,(0,0,0),(40,255,40))
    cv2.imshow("liveredcolor",redimg)
    if cv2.waitKey(10) & 0xff == ord('q'):
      break
cv2.destroyAllWindows()
cap.release()

