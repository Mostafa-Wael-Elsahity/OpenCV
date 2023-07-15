import numpy as np 
import cv2 as cv

cap = cv.VideoCapture(0) # 0 for default camera, 1 for external camera or file name you want to read between ' '

while True: # loop for video capture
    ret, frame = cap.read() # ret is boolean value, frame is image ret is True if frame is available otherwise False 

    width = int(cap.get(3)) # get width of frame  3 is width id of video capture object why int because it came from floating point value
    height = int(cap.get(4)) # get height of frame  4 is height id of video capture object
    
    image = np.zeros(frame.shape, np.uint8) # create black image with same shape as frame image  uint8 is datatype of image (0-255) 8 bit 
    smaller_frame = cv.resize(frame, (0, 0), fx=0.5, fy=0.5) # resize frame to half of its size
    # be careful when resize image because it will change shape of image and you can't paste it to another image with different shape
    image[:height//2,:width//2] = cv.rotate(smaller_frame, cv.ROTATE_180) # paste smaller_frame to 0th to height//2th row of image from 0th to width//2th pixel
    image[height//2:,:width//2] = smaller_frame # paste smaller_frame to height//2th to heightth row of image from 0th to width//2th pixel
    image[:height//2,width//2:] = cv.rotate(smaller_frame, cv.ROTATE_180) # paste smaller_frame to 0th to height//2th row of image from width//2th to widthth pixel
    image[height//2:,width//2:] = smaller_frame # paste smaller_frame to height//2th to heightth row of image from width//2th to widthth pixel

    
    cv.imshow('Frame', image)

    if cv.waitKey(1) == ord('q'): # ord('q') is ASCII value of q, waitKey(1) is wait for 1 millisecond for key press
        break 

cap.release() # release camera
cv.destroyAllWindows() # destroy all windows