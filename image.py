#!/usr/bin/python
import cv2
import numpy as np
a=np.zeros([500,500])
cv2.imwrite('a.png',a)
cv2.imshow('aa',a)
cv2.waitKey(0)
cv2.destroyAllWindows()
