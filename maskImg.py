
# coding: utf-8

# In[1]:


import cv2
import numpy as np
import os

def search(dir):
    files = os.listdir(dir)
    return files


# In[2]:


maskdir = './output_mask/'
styledir = './multistyle/'
outputdir = './croped_'+styledir[2:-1]+


styleimage = search(styledir[:-1])
maskimage = search(maskdir[:-1])



if not os.path.exists(outputdir):
    os.makedirs(outputdir)

for file in styleimage:
    image = cv2.imread(styledir+file)
    mask = cv2.imread(maskdir+file)
    masked_image = cv2.bitwise_and(image, mask)
    tmp = cv2.cvtColor(masked_image, cv2.COLOR_BGR2GRAY)
    _,alpha = cv2.threshold(tmp,9,255,cv2.THRESH_BINARY)
    b, g, r = cv2.split(masked_image)
    rgba = [b,g,r, alpha]
    dst = cv2.merge(rgba,4)
    # save the result
    cv2.imwrite(outputdir+file[:-4]+'.png', dst)

