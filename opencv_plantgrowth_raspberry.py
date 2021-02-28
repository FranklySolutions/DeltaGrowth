#resources
#https://stackoverflow.com/questions/33369832/read-multiple-images-on-a-folder-in-opencv-python/33371454

def get_delta_growth():

    #import dependencies
    import glob
    import cv2
    import numpy as np

    #global value
    image_list = [cv2.imread(file) for file in glob.glob("Photos/time/*")]

    #get the latest image taken
    image = image_list[-1]

    #converting image into hsv color field
    img_hsv = cv2.cvtColor(image,cv2.COLOR_BGR2HSV)

    #setting HSL values
    hue_min = 29
    hue_max = 110
    sat_min = 25
    sat_max = 255
    val_min = 0
    val_max = 255

    #set filter Lower and upper limits
    lower = np.array([hue_min, sat_min, val_min])
    upper = np.array([hue_max, sat_max, val_max])

    #apply filter as mask
    mask = cv2.inRange(img_hsv, lower, upper)

    # blurring mask to eliminate static
    blurred_mask = cv2.GaussianBlur(mask, (5, 5), 5)

    # sum all 1's in the black and white mask
    growth = np.sum(mask > 0)

    #calculate delta growth compared to first image
    delta_growth = ((growth - 11592) / 11592 ) * 100

    #print
    return int(delta_growth)

print(get_delta_growth())