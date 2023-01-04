import cv2
import numpy as np
from numpy.core.fromnumeric import resize

def empty(a):
    pass

cv2.namedWindow('Filter')
cv2.resizeWindow("Filter", 500,440)
cv2.createTrackbar('Red min', 'Filter',0,255,empty )
cv2.createTrackbar('Red max', 'Filter',0,255,empty )

cv2.createTrackbar('Blue min', 'Filter',0,255,empty )
cv2.createTrackbar('Blue max', 'Filter',0,255,empty )

cv2.createTrackbar('Green min', 'Filter',0,255,empty )
cv2.createTrackbar('Green max', 'Filter',0,255,empty )

cv2.createTrackbar('count', 'Filter',0,500,empty )

count= 0
while True:
    r_min = cv2.getTrackbarPos('Red min', 'Filter')
    r_max = cv2.getTrackbarPos('Red max', 'Filter')

    b_min = cv2.getTrackbarPos('Blue min', 'Filter')
    b_max = cv2.getTrackbarPos('Blue max', 'Filter')

    g_min = cv2.getTrackbarPos('Green min', 'Filter')
    g_max = cv2.getTrackbarPos('Green max', 'Filter')

    count = cv2.getTrackbarPos('count', 'Filter')

    lower = np.array([r_min, b_min, g_min]) 
    upper = np.array([r_max, b_max, g_max]) 

    # lower = np.array([ 26, 142, 151])
    # upper = np.array([ 87, 210, 221])

    # lower = np.array([ 19, 71, 146])
    # upper = np.array([ 75, 160, 255])

    # lower = np.array([ 30, 80, 140])
    # upper = np.array([ 80, 160, 255])

    image = cv2.imread("frames_final/"+str(count)+".jpeg")
    mask = cv2.inRange(image, lower, upper)
    result = cv2.bitwise_and(image, image, mask=mask)
    
    cv2.imshow('mask', result)
    cv2.imshow('org',image)
    cv2.waitKey(100)
    print(count)
    # cv2.imwrite('D:/etme/Ball-20211104T173348Z-001/final/masks_final/%d.jpeg'%count, mask)
    # cv2.imwrite('D:/etme/Ball-20211104T173348Z-001/final/result/%d.jpeg'%count, result)
    count=count+1
    

#[ 25 114 142] [ 83 203 227]
#[ 25 112 147] [ 85 204 235]
