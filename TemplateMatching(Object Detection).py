import numpy as np
import cv2 as cv

image = cv.resize(cv.imread('OpenCV/soccer_practice.jpg', 0), (0,0), fx=0.7, fy=0.7) # 0 for grayscale, 1 for color, -1 for unchanged
template = cv.resize(cv.imread('OpenCV/shoe.png', 0), (0,0), fx=0.7, fy=0.7) # 0 for grayscale, 1 for color, -1 for unchanged
# u need to resize the template to match the image with the same scale (fx and fy) 


h, w = template.shape # get height and width of template

methods = [cv.TM_CCOEFF, cv.TM_CCOEFF_NORMED, cv.TM_CCORR,   # template matching methods
            cv.TM_CCORR_NORMED, cv.TM_SQDIFF, cv.TM_SQDIFF_NORMED] 

for method in methods:  # loop through methods
    image1 = image.copy() # reset image
    result = cv.matchTemplate(image1, template, method) # match template to image using method matching method
    min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result) # get min and max values and locations
    if method in [cv.TM_SQDIFF, cv.TM_SQDIFF_NORMED]: # if method is TM_SQDIFF or TM_SQDIFF_NORMED
        location = min_loc # location is min_loc
    else: 
        location = max_loc # location is max_loc

    cv.rectangle(image1, location, (location[0] + w, location[1] + h), 255, 2) # draw rectangle around location
    cv.imshow('Match', image1) # show image
    cv.waitKey(0) # wait for key press
    cv.destroyAllWindows() # destroy all windows

''' 
matching methods: example 
image : 
[
    [255,255,255,255],
    [255,255,255,255],
    [255,255,255,255],
    [255,255,255,255]
]
template :
[
    [255,255],
    [255,255]
]
result : 
[
    [1,1,1],
    [1,1,1],
    [1,1,1]
]
any index indicate the the template matches the image at that index
'''
