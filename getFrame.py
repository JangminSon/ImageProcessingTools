
# coding: utf-8

import cv2
import os

vidName = 'vid.mp4'         #Set Video name
vidcap = cv2.VideoCapture(vidName)      
success,image = vidcap.read()
count = 0
success = True

while success:
    success,image = vidcap.read()
    if success is None:
        break
    print('Read a new frame: ', success)
    os.mkdir(vidName[:-4])
    cv2.imwrite("./"+vidName+"/%d.jpg" % count, image)     # dir you want to save
    count += 1

