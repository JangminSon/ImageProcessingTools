
# coding: utf-8

# In[1]:


import numpy as np
import cv2
import imutils
import os


# In[2]:


def search(dirname):
    filenames = os.listdir(dirname)
    return filenames;


# In[3]:


files = search(inDIR)
inDIR = './faceframe'
outDIR = './grapcut'
# print(files[5][:-4])


# In[7]:


for file in files:

    YOURFILE = inDIR+'/'+file
    img = cv2.imread(YOURFILE)
    img = imutils.resize(img, height=910, width=512)
    mask = np.zeros(img.shape[:2], np.uint8)
    mask_b = np.zeros(img.shape, np.uint8)
    bgdModel = np.zeros((1, 65), np.float64)
    fgdModel = np.zeros((1, 65), np.float64)
    r = (117, 98, 262, 811) #Rect for Object

    #If you want to get X,Y axis
    #Uncomment lines below
#     r = cv2.selectROI(img)
#     print(r)
#     for a in r:
#         print (a)

    rect = (int(r[0]), int(r[1]), int(r[0] + r[2]), int(r[1] + r[3]))
#     imCrop = img[int(r[1]):int(r[1] + r[3]), int(r[0]):int(r[0] + r[2])]


    cv2.grabCut(img, mask, rect, bgdModel, fgdModel, 5, cv2.GC_INIT_WITH_RECT)
    mask2 = np.where((mask == 2) | (mask == 0), 0, 1).astype('uint8')
    img = img * mask2[:, :, np.newaxis]
    mask_b[np.where((mask_b == [0, 0, 0]).all(axis=2))] = [233,170,89]
#     cv2.imshow("image", img)
#     cv2.imwrite("output2.png",img)
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()
#     tmp = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#     _,alpha = cv2.threshold(tmp,0,255,cv2.THRESH_BINARY)
#     b, g, r = cv2.split(img)
#     rgba = [b,g,r, alpha]
#     dst = cv2.merge(rgba,4)
    cv2.imwrite(outDIR+'/'+file[:-4]+".jpg", img)


# In[4]:


YOURFILE = '8.jpg'
img = cv2.imread(YOURFILE)
img = imutils.resize(img, height=280, width=440)
mask = np.zeros(img.shape[:2], np.uint8)
mask_b = np.zeros(img.shape, np.uint8)
bgdModel = np.zeros((1, 65), np.float64)
fgdModel = np.zeros((1, 65), np.float64)
r = (70, 48, 210, 556) #Rect for Object

#If you want to get X,Y axis
#Uncomment lines below
r = cv2.selectROI(img)
print(r)
for a in r:
    print (a)

rect = (int(r[0]), int(r[1]), int(r[0] + r[2]), int(r[1] + r[3]))
imCrop = img[int(r[1]):int(r[1] + r[3]), int(r[0]):int(r[0] + r[2])]


cv2.grabCut(img, mask, rect, bgdModel, fgdModel, 5, cv2.GC_INIT_WITH_RECT)
mask2 = np.where((mask == 2) | (mask == 0), 0, 1).astype('uint8')


img = img * mask2[:, :, np.newaxis]
mask_b[np.where((mask_b == [0, 0, 0]).all(axis=2))] = [233,170,89]
cv2.imwrite('facegrap.jpg', img)
# #     cv2.imshow("image", img)
# #     cv2.imwrite("output2.png",img)
# #     cv2.waitKey(0)
# #     cv2.destroyAllWindows()
# tmp = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# _,alpha = cv2.threshold(tmp,0,255,cv2.THRESH_BINARY)
# b, g, r = cv2.split(img)
# rgba = [b,g,r, alpha]
# dst = cv2.merge(rgba,4)
# cv2.imwrite('./hello.jpg', dst)

