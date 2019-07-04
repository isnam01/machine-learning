#!/usr/bin/python
import cv2
casclf=cv2.CascadeClassifier('face.xml')
cap=cv2.VideoCapture(0)
i=1
while cap.isOpened():
    status,frame=cap.read()
    face=casclf.detectMultiScale(frame,1.15,5)
    for x,y,h,w in face:
        cv2.rectangle(frame,(x,y),(x+h,y+w),(0,255,255),2)  
        img1=frame[y:y+w,x:x+h]
        cv2.imwrite("abcd"+str(i)+".jpeg",img1)
    cv2.imshow("face",frame)
    i+=1
    if cv2.waitKey(10) & 0xff == ord('q'):
         break
cv2.destroyAllWindows()
cap.release()

