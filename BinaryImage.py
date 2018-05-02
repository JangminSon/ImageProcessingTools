import numpy as np
import os
import cv2 #this is the main openCV class, the python binding file should be in /pythonXX/Lib/site-packages
from matplotlib import pyplot as plt

files = os.listdir("./photoid/")
imgpath = "./photoid/"
threshhold_val = 180
kernel_size = (8,8)

for file in files:
    gwash = cv2.imread(imgpath+file) #import image
    gwashBW = cv2.cvtColor(gwash, cv2.COLOR_BGR2GRAY) #change to grayscale

    ret,thresh1 = cv2.threshold(gwashBW,threshhold_val,255,cv2.THRESH_BINARY) #
    kernel = np.ones(kernel_size,np.uint8) #square image kernel used for erosion
    erosion = cv2.erode(thresh1, kernel,iterations = 1) #refines all edges in the binary image
    opening = cv2.morphologyEx(erosion, cv2.MORPH_OPEN, kernel)
    closing = cv2.morphologyEx(opening, cv2.MORPH_CLOSE, kernel) #this is for further removing small noises and holes in the image
#     plt.imshow(closing, 'gray') #Figure 2
#     plt.xticks([]), plt.yticks([])
#     plt.show()
#     plt.imshow(opening, 'gray') #Figure 2
#     plt.xticks([]), plt.yticks([])
#     plt.show()
    image, contours, hierarchy = cv2.findContours(closing,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE) #find contours with simple approximation
    areas = [] #list to hold all areas
    max =0
    for contour in contours:
        ar = cv2.contourArea(contour)
        if(ar>max):
            max=ar
        areas.append(ar)

    max_area_index = areas.index(max) #index of the list element with largest area

    bg = np.zeros(opening.shape)
    cv2.drawContours(bg,contours,max_area_index , (255,255,255), 1)
    cv2.fillPoly(bg, pts =[contours[max_area_index]], color=(255,255,255))

#     plt.imshow(bg, 'gray') #Figure 2
#     plt.xticks([]), plt.yticks([])
#     plt.show()
    cv2.imwrite("./result/"+file.split('.')[0]+'_lenagray.png', 255-bg)

    
