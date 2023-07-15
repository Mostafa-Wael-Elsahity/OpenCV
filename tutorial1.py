import cv2 as cv

# Reading Images imread default load image as BGR format
img = cv.imread('OpenCV/myPhoto.jpg', 1) # 0 for grayscale, 1 for color, -1 for unchanged
'''
-1 : cv.IMREAD_UNCHANGED : Loads image as such including alpha channel images and loads as 32-bit image (8-bit images are converted to 32-bit).
0 : cv.IMREAD_GRAYSCALE : Loads image in grayscale mode.
1 : cv.IMREAD_COLOR : Loads a color image. Any transparency of image will be neglected. It is the default flag.
'''
# when set (0,0) u can set fx=0.5 and fy=0.5 to resize image to half of its size fractions
img = cv.resize(img, (0, 0), fx=0.5, fy=0.3) # resize image to half of its size

# rotate image 
img = cv.rotate(img, cv.ROTATE_90_COUNTERCLOCKWISE) # rotate image 90 degree clockwise

# save image 
cv.imwrite('OpenCV/myPhoto1.jpg', img) # save image as myPhoto.jpg

# Displaying Images imshow default load image as BGR format with window name as 'image' and image will be closed when any key is pressed or wait for 5 seconds
cv.imshow('Image', img) 
cv.waitKey(0) # 0 for infinite time, 5 for 5 seconds
cv.destroyAllWindows()

