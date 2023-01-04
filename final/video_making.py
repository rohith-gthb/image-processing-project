# import cv2
# import os

# images = os.listdir('result')
# for i in range(len(images)):
#     images[i] = 'result/'+images[i]

import cv2
import numpy as np
import glob

frameSize = (960, 540)

out = cv2.VideoWriter('output_video.avi',cv2.VideoWriter_fourcc(*'DIVX'), 60, frameSize)

for filename in glob.glob('D:/etme/Ball-20211104T173348Z-001/final/result/*.jpeg'):
    img = cv2.imread(filename)
    out.write(img)

out.release()