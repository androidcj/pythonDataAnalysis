#coding:utf-8
import numpy as np

#图像卷积操作
def convole(image,weight):
    heigh,width = image.shape
    h,w = weight.shape
    height_new = heigh-h+1
    width_new = width-w+1
    image_new = np.zeros((height_new,width_new),dtype=np.float)
    for i in range(height_new):
        for j in range(width_new):
            image_new[i,j] = np.sum(image[i:i+h,j:j+w] * weight)
    image_new = image_new.clip(0,255)
    image_new = np.rint(image_new).astype('uint8')
    return image_new  
    
    
    