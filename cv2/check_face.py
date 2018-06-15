# video 

import cv2  
import numpy
import matplotlib.pyplot as plot

cap = cv2.VideoCapture(0)
while(1):
    # get a frame
    ret, frame = cap.read()

    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    faces = face_cascade.detectMultiScale(frame_gray, scaleFactor=1.2, minNeighbors=3, minSize=(10, 10))

    for(x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+w),(0,255,0),2)
   
    cv2.imshow("capture", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows() 