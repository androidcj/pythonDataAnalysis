#coding:utf-8
'''
Created on 2018年4月5日

得到像素的分布图

@author: win7
'''

from skimage import data
from skimage import exposure
from matplotlib import pyplot as plt

def run_main():
    image_data = data.camera()
    hist,bin_centers = exposure.histogram(image_data)
    fig,ax = plt.subplots(ncols=1)
    ax.fill_between(bin_centers,hist)
    plt.show()
    return '';



if __name__ == '__main__':
    run_main()