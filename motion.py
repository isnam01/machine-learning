#!/usr/bin/python
import cv2
cap=cv2.VideoCapture(0)
tp1=cap.read()[1]
tp2=cap.read()[1]
tp3=cap.read()[1]
gray1=cv2.cvtColor(tp1,cv2.COLOR_BGR2GRAY)
gray2=cv2.cvtColor(tp2,cv2.COLOR_BGR2GRAY)
gray3=cv2.cvtColor(tp3,cv2.COLOR_BGR2GRAY)
def img_diff(x,y,z):
    d1=cv2.absdiff(x,y)
    d2=cv2.absdiff(y,z)
    finalimg=cv2.bitwise_and(d1,d2)
    return finalimg


while cap.isOpened():
    status,frame=cap.read()
    motionimg=img_diff(gray1,gray2,gray3)
    gray1=gray2
    gray2=gray3
    gray3=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow("liveredcolor",frame)
    cv2.imshow("liveredcolor",motionimg)
    if cv2.waitKey(10) & 0xff == ord('q'):
      break
cv2.destroyAllWindows()
cap.release()
