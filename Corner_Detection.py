import numpy as np 
import cv2 as cv

image = cv.imread('OpenCV/chessBoard.jpg') # 0 for grayscale, 1 for color, -1 for unchanged
image = cv.resize(image, (0,0), fx=0.75, fy=0.75) # resize image to half of its size
gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY) # convert image to grayscale

corners = cv.goodFeaturesToTrack(gray, 100, 0.01, 10) # 100 is max corners to detect, 0.01 is minimum quality level, 10 is minimum distance between corners
corners = np.int0(corners) # convert float values to int

for corner in corners: # draw circles at corners
    x, y = corner.ravel() # ravel() is used to flatten the array
    cv.circle(image, (x, y), 5, (255, 0, 0), -1) # draw circle at (x, y) with radius 5, color (255, 0, 0) and fill the circle

for i in range(len(corners)): # draw lines between corners
    for j in range(i + 1, len(corners)):
        corner1 = tuple(corners[i][0]) # convert array to tuple
        corner2 = tuple(corners[j][0]) # convert array to tuple
        color = tuple(map(lambda x: int(x), np.random.randint(0, 255, size=3))) # generate random color
        cv.line(image, corner1, corner2, color, 1) # draw line between corner1 and corner2 with color

cv.imshow('Original Image', image)
cv.waitKey(0)
cv.destroyAllWindows()

