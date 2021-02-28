# resources
# https://stackoverflow.com/questions/33369832/read-multiple-images-on-a-folder-in-opencv-python/33371454
#https://stackoverflow.com/questions/7336096/python-glob-without-the-whole-path-only-the-filename

# import dependencies
import glob
import cv2
import numpy as np
import os

# global value
image_list = [cv2.imread(file) for file in glob.glob("Photos/time_total/*")]
name_list = [os.path.basename(x) for x in glob.glob("Photos/time_total/*")]

# creating csv file
f = open("time_total_analysis.csv", "w")

#set value for i
i=0

while i < len(image_list):
    # get the latest image taken
    image = image_list[i]

    # converting image into hsv color field
    img_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # setting HSL values
    hue_min = 20
    hue_max = 110
    sat_min = 9
    sat_max = 255
    val_min = 0
    val_max = 255

    # set filter Lower and upper limits
    lower = np.array([hue_min, sat_min, val_min])
    upper = np.array([hue_max, sat_max, val_max])

    # apply filter as mask
    mask = cv2.inRange(img_hsv, lower, upper)

    # blurring mask to eliminate static
    blurred_mask = cv2.GaussianBlur(mask, (5, 5), 5)

    # sum all 1's in the black and white mask
    growth = np.sum(mask > 0)

    # calculate delta growth compared to first image (old)
    # delta_growth = ((growth - 11592) / 11592) * 100

    # calculate delta growth compared to first image
    delta_growth = ((growth - 49285) / 49285) * 100

    # print
    print(name_list[i], end=",")
    print(growth, end=",")
    print(int(delta_growth))

    #writing to file
    f.write(name_list[i] + "," + str(growth)+ "," + str(int(delta_growth)) + "\n")



    #putting text
    font = cv2.FONT_HERSHEY_SIMPLEX
    bottomLeftCornerOfText = (10, 450)
    fontScale = 1
    fontColor = (255, 255, 10)
    lineType = 2

    cv2.putText(blurred_mask, "Delta growth = "+ str(int(delta_growth)) + "%",
                bottomLeftCornerOfText,
                font,
                fontScale,
                fontColor,
                lineType)

    cv2.imshow("image", blurred_mask)
    cv2.waitKey(100)

    # saving file
    name_list[i] = "Photos/time_total_mask/" + name_list[i]
    cv2.imwrite(name_list[i],blurred_mask)

    #iterate i
    i=i+1

#close file
f.close()