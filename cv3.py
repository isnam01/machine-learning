#!/usr/bin/bash
import cv2
img1=cv2.imread("dog3.jpeg")
img2=cv2.imread("dog2.jpeg")
d2=cv2.absdiff(img1,img2)
cv2.imshow("abc",d2)
cv2.imshow("abc1",img1+img2)
if cv2.waitKey(0) & 0xff ==("q"):
    cv2.release()
    cv2.closeAllWindows()
