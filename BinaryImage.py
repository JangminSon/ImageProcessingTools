
# coding: utf-8

# In[2]:


import numpy as np
import cv2 #this is the main openCV class, the python binding file should be in /pythonXX/Lib/site-packages
from matplotlib import pyplot as plt

gwash = cv2.imread("out2.png") #import image
gwashBW = cv2.cvtColor(gwash, cv2.COLOR_BGR2GRAY) #change to grayscale
# gwashOrg = cv2.cvtColor(gwash, )
img = cv2.cvtColor( gwash, cv2.COLOR_RGB2GRAY )
cv2.imwrite( "grey.jpg", img )

plt.imshow(gwashBW, 'gray') #this is matplotlib solution (Figure 1)
plt.xticks([]), plt.yticks([])
plt.show()
gwash.shape


# In[2]:


ret,thresh1 = cv2.threshold(gwashBW,38,255,cv2.THRESH_BINARY) #
kernel = np.ones((5,5),np.uint8) #square image kernel used for erosion
erosion = cv2.erode(thresh1, kernel,iterations = 1) #refines all edges in the binary image

opening = cv2.morphologyEx(erosion, cv2.MORPH_OPEN, kernel)
closing = cv2.morphologyEx(opening, cv2.MORPH_CLOSE, kernel) #this is for further removing small noises and holes in the image
plt.imshow(opening, 'gray') #Figure 2
plt.xticks([]), plt.yticks([])
plt.show()

plt.imshow((255-closing), 'gray') #Figure 2
plt.xticks([]), plt.yticks([])
plt.show()

# background = np.zeros(img.shape)
# cv2.imshow('asd', 255-background) #Figure 3
# cv2.drawContours(closing, contours, -1, (255, 255, 255), 4)

cv2.waitKey(0)
image, contours, hierarchy = cv2.findContours(closing,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE) #find contours with simple approximation




cv2.imshow('cleaner', image) #Figure 3
cv2.drawContours(image, contours, 1, (255, 255, 255), 4)
cv2.waitKey(0)


# In[34]:


areas = [] #list to hold all areas

for contour in contours:
  ar = cv2.contourArea(contour)
  areas.append(ar)

print(areas)

areas.sort()
print(areas[-2])

max_area = areas[-2]
print(max_area)
max_area_index = areas.index(max_area) #index of the list element with largest area
print (max_area_index)

cnt = contours[max_area_index] #largest area contour

bg = np.zeros(opening.shape)
cv2.drawContours(bg,contours,max_area_index+1 , (255,255,255), 1)
cv2.fillPoly(bg, pts =[contours[max_area_index+1]], color=(255,255,255))
cv2.imshow('cleaner', bg)
cv2.waitKey(0)
cv2.destroyAllWindows()
# areas = [] #list to hold all areas
# for contour in contours:
#   ar = cv2.contourArea(contour)
#   areas.append(ar)

# max_area = max(areas)
# max_area_index = areas.index(max_area) #index of the list element with largest area

# cnt = contours[max_area_index] #largest area contour

# cv2.drawContours(closing, [cnt], 0, (255, 255, 255), 3, maxLevel = 0)
# cv2.imshow('cleaner', closing)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# plt.imshow(closing, 'gray') #Figure 2
# plt.xticks([]), plt.yticks([])
# plt.show()
cv2.imwrite('lenagray.png', bg)

