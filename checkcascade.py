import numpy as np
import cv2

face_cascade = cv2.CascadeClassifier('aastha-first-cascade.xml')

cap = cv2.VideoCapture(0)

while 1:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 4, 4)
    
    # add this
    # image, reject levels level weights.
    # add this

    for (x,y,w,h) in faces:
        font=cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img,'Aastha',(x-w//12,y-h//12),font,1,(0,255,255),2,cv2.LINE_AA)
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)

    cv2.imshow('img',img)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
