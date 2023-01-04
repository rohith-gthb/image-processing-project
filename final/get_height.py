from threading import local
import cv2
import os
import numpy as np
from PIL import Image
from tqdm import tqdm 
import pandas as pd

data = []

def check(img):
    y,x = img.shape
    for i in range(-1,-y,-1):
        for j in range(-1,-x,-1):
            if(img[i][j]!=0):
                data.append(-i)
                return 
    data.append(0)
    return 

def get_e(max):
    l=[]
    for i in range(0, len(max)-1):
        if(max[i+1]!=0):
            l.append(max[i]/max[i+1])
            # if(max[i]/max[i+1]!=1):
                
    return l

def local_max(data):
    local_max = []
    min = 500
    for i in range(1,len(data)-1,1):
        if(min>data[i]):
            min = data[i]
        if(data[i-1]<data[i]):
            if(data[i+1]<data[i]):
                local_max.append(data[i])
    
    local_max.append(min)
    return local_max


l = os.listdir('masks_final')
for i in tqdm(range(502)):
    img = Image.open('masks_final/'+str(i)+'.jpeg')
    width, height = img.size
    # Setting the points for cropped image

    # left = 150
    # top = 150
    # right = 450
    # bottom = height
    # im1 = img.crop((left, top, right, bottom))
    # im1 = np.array(im1)
    img = np.array(img)
    # cv2.circle(im1, (130,240), 2, (255,0,0), 2)
    # cv2.imshow('r', im1[100:150, 120:170])
    # print(im1.size)
    t=check(img)
    # x,y,found = t[0],t[1],t[2] 
    # if found:
    #     print(x,y)
    # cv2.imshow('x',im1[-420:-50, -100:-1])
    # cv2.waitKey(150)

print(len(data))
# print(data[0], data[9])
pd.DataFrame(data).to_csv('height.csv')

heights = local_max(data)

floor_y = np.array(heights[-1])
ball_y = np.array(heights[:-1])

e = get_e(ball_y-floor_y)
pd.DataFrame(e).to_excel('e.xlsx', index=False)
