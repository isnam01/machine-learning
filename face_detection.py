#!/usr/bin/python
import cv2
casclf=cv2.CascadeClassifier('face.xml')
casclf=cv2.CascadeClassifier('eyes.xml')
#img=cv2.imread(imagename)
cap=cv2.VideoCapture(0)
while cap.isOpened():
    status,frame=cap.read()
    face= casclf.detectMultiScale(frame,1.15,5)
    #classifier tuning accuracy parameter
    eyes= casclf.detectMultiScale(frame,1.15,5)
    #print(face)
    for x,y,h,w in face:
        cv2.rectangle(frame,(x,y),(x+h,y+w),(0,0,255),2)
        for a,b,c,d in eyes:
           cv2.rectangle(frame,(a,b),(a+c,b+d),(0,0,255),2)
    cv2.imshow("face",frame)
    if cv2.waitKey(10) & 0xff == ord('q'):
        break
cv2.destroyAllWindows()
cap.release()

