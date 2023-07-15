import cv2 as cv 
import random as rd


img = cv.imread('OpenCV/myPhoto.jpg', -1)

print(img) # print image as numpy array
print(type(img)) # print type of image
print(img.shape) # print shape of image (height, width, channels) channels are color space of image (RGB, BGR, HSV, etc)

# blue green red (BGR) color space 0-255 (0 is dark, 255 is bright) 
# 0,0,0 is black
# 255,255,255 is white
# 255,0,0 is blue
# 0,255,0 is green
# 0,0,255 is red
# 255,255,0 is yellow
# 255,0,255 is magenta
# 0,255,255 is cyan 
# and so on 
# image is store in 3D array (height, width, channels)

# when manipulate image we change pixel value of image 

# print(img[0]) # print first row of image
# print(img[0][0]) # print first pixel of image
# print(img[0][0][0]) # print first pixel of image blue value
# print(img[0][0][1]) # print first pixel of image green value
# print(img[0][0][2]) # print first pixel of image red value
print(img[257][50:100]) # print 257th row of image from 50th to 100th pixel

copyPart = img[500:700, 600:900] # copy 500th to 700th row of image from 600th to 900th pixel 
img[0:200, 0:300] = copyPart # paste copyPart to 0th to 200th row of image from 0th to 300th pixel



# for i in range(100): # print 100th row of image
#     for j in range(img.shape[1]): # print all pixel of 100th row of image
#         img[i][j] = [rd.randint(0, 255), rd.randint(0, 255), rd.randint(0, 255)] # change pixel value of image

cv.imshow('Image', img)
cv.waitKey(0)
cv.destroyAllWindows()
