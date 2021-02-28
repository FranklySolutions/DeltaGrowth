#resources used in developing this app
#https://stackoverflow.com/questions/47494350/count-total-number-of-white-pixels-in-an-image-is-throwing-an-error/51077696

import cv2
import numpy as np

#reading image
#image = cv2.imread("Photos/lettuce_normal_licht_grown.jpg")
#image = cv2.imread("Photos/lettuce_normal_licht_reference.jpg")
image = cv2.imread("Photos/time_total/2021-01-19_0615.jpg")

#rescaling image
scale_percent = 60 # percent of original size
width = int(image.shape[1] * scale_percent / 100)
height = int(image.shape[0] * scale_percent / 100)
dim = (width, height)
resized = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)

#converting image into hsv
img_hsv = cv2.cvtColor(resized,cv2.COLOR_BGR2HSV)

# blurrign image to reduce complexity
#blurred_hsv = cv2.GaussianBlur(img_hsv, (5, 5), 10)
#blurred_bgr = cv2.GaussianBlur(resized, (5, 5), 10)


#empty function
def empty(a):
    pass

#Creating trackbars
cv2.namedWindow("trackbars")
cv2.resizeWindow("trackbars",640,240)
cv2.createTrackbar("hue min","trackbars",31,179,empty)
cv2.createTrackbar("hue max","trackbars",69,179,empty)
cv2.createTrackbar("sat min","trackbars",42,255,empty)
cv2.createTrackbar("sat max","trackbars",255,255,empty)
cv2.createTrackbar("val min","trackbars",0,255,empty)
cv2.createTrackbar("val max","trackbars",255,255,empty)

#getting trackbar value
while True:
    hue_min = cv2.getTrackbarPos("hue min","trackbars")
    hue_max = cv2.getTrackbarPos("hue max","trackbars")
    sat_min = cv2.getTrackbarPos("sat min","trackbars")
    sat_max = cv2.getTrackbarPos("sat max","trackbars")
    val_min = cv2.getTrackbarPos("val min","trackbars")
    val_max = cv2.getTrackbarPos("val max","trackbars")

    #setting
    lower = np.array([hue_min,sat_min,val_min])
    upper = np.array([hue_max, sat_max, val_max])
    mask = cv2.inRange(img_hsv, lower, upper)
    #mask = cv2.bitwise_not(mask)
    #print(hue_min,hue_max,sat_min,sat_max,val_min,val_max)

    #apply mask
    bgr_mask_applied = cv2.bitwise_and(resized,resized,mask=mask)

    #blurr mask to even out the picture
    blurred_mask = cv2.GaussianBlur(mask, (5, 5), 5)

    #showing results
    cv2.imshow("BGR mask applied",bgr_mask_applied)
    cv2.imshow("BGR", resized)
    cv2.imshow("blurred mask", blurred_mask)

    x = np.sum(mask > 0)
    print(x)
    cv2.waitKey(1)