import numpy as np
import cv2 as cv

cap = cv.VideoCapture(0) # capture video from webcam
face_cascade = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_frontalface_default.xml') # load face cascade
eye_cascade = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_eye.xml') # load eye cascade

while True: # loop forever
    ret, frame = cap.read() # read frame from webcam
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY) # convert frame to grayscale
    faces = face_cascade.detectMultiScale(gray, 1.3, 5) # detect faces in frame first parameter is frame, second is scale factor, third is min neighbors
    for (x, y, w, h) in faces: # for each face
        cv.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2) # draw rectangle around face
        roi_gray = gray[y:y + h, x:x + w] # get region of interest in grayscale
        roi_color = frame[y:y + h, x:x + w] # get region of interest in color
        eyes = eye_cascade.detectMultiScale(roi_gray) # detect eyes in region of interest
        for (ex, ey, ew, eh) in eyes: # for each eye
            cv.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2) # draw rectangle around eye


    cv.imshow('Webcam', frame) 
    if cv.waitKey(1) == ord('q'): 
        break 

cap.release()
cv.destroyAllWindows()