#coding:utf-8
'''
Created on 2018年4月5日

得到红色通道下的图片

@author: win7
'''
from skimage import data
from matplotlib import pyplot as plt


def run_main():
    color_image = data.chelsea()
    
    red_chanel = color_image[:,:,0]
    print(color_image.shape)
    plt.imshow(red_chanel)
    plt.show()
    return ''


if __name__ == '__main__':
    run_main()