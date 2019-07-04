#!/usr/bin/bash
import cv2
img=cv2.imread("dog1.jpeg")
img1=img[50:150,100:250]
res = cv2.resize(img1, dsize=(300,300), interpolation=cv2.INTER_CUBIC)
res1=res[50:150,100:250]
res2 = cv2.resize(res1, dsize=(300,300), interpolation=cv2.INTER_CUBIC)
img[50:70,100:150]=res2[50:70,100:150]
cv2.imshow("a",img)
if cv2.waitKey(0) & 0xff == ord('q'):
    cv2.release()
    cv2.destroyAllWindows()

