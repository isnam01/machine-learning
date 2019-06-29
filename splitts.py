#!/usr/bin/python
import cv2
img=cv2.imread("/home/mansi/Desktop/work/pexels-photo-462118.jpeg")
x,y,z=cv2.split(img)
cv2.imshow("p",z)
cv2.waitKey(1100)
cv2.destroyAllWindows()
cv2.imshow("p",x)
cv2.waitKey(1100)
cv2.destroyAllWindows()
cv2.imshow("p",y)
cv2.waitKey(1200)
cv2.destroyAllWindows()



