#!/usr/bin/python
import cv2
img1=cv2.imread("dog3.jpeg")
img2=cv2.imread("dog2.jpeg")
f=cv2.addWeighted(img1,0.7,img2,0.7,0)
cv2.imshow("a",f)
if cv2.waitKey(0) & 0xff == ord('q'):
    cv2.destroyAllWindows()
