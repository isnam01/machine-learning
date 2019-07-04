#!/usr/bin/bash
import cv2
img=cv2.imread("dog1.jpeg")
img1=img[50:150,100:250]
res = cv2.resize(img1, dsize=(400,400), interpolation=cv2.INTER_CUBIC)
cv2.imshow("a",res)
if cv2.waitKey(0) & 0xff == ord('q'):
    cv2.release()
    cv2.destroyAllWindows()
