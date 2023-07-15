import numpy as np 
import cv2 as cv

cap = cv.VideoCapture(0) # 0 for default camera, 1 for external camera or file name you want to read between ' '

while True: # loop for video capture
    ret, frame = cap.read() # ret is boolean value, frame is image ret is True if frame is available otherwise False 
    width = int(cap.get(3)) # get width of frame  3 is width id of video capture object why int because it came from floating point value
    height = int(cap.get(4)) # get height of frame  4 is height id of video capture object
    
    # cartesian plan is different in image processing than in mathematics 
    # in image processing origin is at top left corner of image 
    # x axis is horizontal and y axis is vertical 
    # x axis is from left to right and y axis is from top to bottom 
    # x axis is width and y axis is height 
    # x axis is from 0 to width-1 and y axis is from 0 to height-1

    # image = cv.line(frame, (0,0), (width,height), (255,0,0), 10) # draw line on frame from (0,0) to (width,height) with color (255,0,0) blue and thickness 10
    # image = cv.line(image, (width,0), (0,height), (0,255,0), 10) # draw line on frame from (0,0) to (width,height) with color (255,0,0) blue and thickness 10
    # image = cv.line(image, (width//2,0), (width//2,height), (0,0,255), 10) # draw line on frame from (0,0) to (width,height) with color (255,0,0) blue and thickness 10
    
    # image =cv.rectangle(image, (100,100), (200,200), (128,128,128), 10) # draw rectangle on frame from (100,100) to (200,200) with color (128,128,128) gray and thickness 10 if u want to fill this rectangle pass thickness -1
    
    # image = cv.circle(image, (width//2,height//2), 50, (0,0,255), 10) # draw circle on frame with center (width//2,height//2) and radius 50 with color (0,0,255) red and thickness 10 if u want to fill this circle pass thickness -1
    image = frame
    font = cv.FONT_HERSHEY_COMPLEX # font type
    image = cv.putText(image, 'Mostafa Wael!', (10, height-10), font, 1, (0,0,255), 1, cv.LINE_AA) # put text on frame with text 'Mostafa Wael!' and position (10, height-10) and font type font and font scale 1 and color (0,0,255) red and thickness 1 and line type cv.LINE_AA
    cv.imshow('Frame', image)

    if cv.waitKey(1) == ord('q'): # ord('q') is ASCII value of q, waitKey(1) is wait for 1 millisecond for key press
        break 

cap.release() # release camera
cv.destroyAllWindows() # destroy all windows