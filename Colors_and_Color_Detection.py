import numpy as np 
import cv2 as cv

cap = cv.VideoCapture(0) # 0 for default camera, 1 for external camera or file name you want to read between ' '

while True: # loop for video capture
    ret, frame = cap.read() # ret is boolean value, frame is image ret is True if frame is available otherwise False 
    width = int(cap.get(3)) # get width of frame  3 is width id of video capture object why int because it came from floating point value
    height = int(cap.get(4)) # get height of frame  4 is height id of video capture object
    
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV) # convert frame from BGR to HSV heigh saturation value and lightness

    lower_blue = np.array([90,50,50]) # lower bound of blue color in HSV
    upper_blue = np.array([130,255,255]) # upper bound of blue color in HSV
    mask = cv.inRange(hsv, lower_blue, upper_blue) # create mask for blue color in frame
    result = cv.bitwise_and(frame, frame, mask=mask) # apply mask on frame

    cv.imshow('Frame', result) # show frame
    cv.imshow('Mask', mask) # show mask

    if cv.waitKey(1) == ord('q'): # ord('q') is ASCII value of q, waitKey(1) is wait for 1 millisecond for key press
        break 

cap.release() # release camera
cv.destroyAllWindows() # destroy all windows