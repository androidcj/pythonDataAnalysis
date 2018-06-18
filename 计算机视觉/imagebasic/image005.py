#coding:utf-8

'''
直方图均衡化
@author: win7
'''

from skimage import data
from skimage import exposure

from matplotlib import pyplot as plt


def run_main():
    image = data.camera()
    equalize = exposure.equalize_hist(image)
    hist3,bin_center3= exposure.histogram(equalize)
    
    fig,(ax1,ax2) = plt.subplots(ncols=2,figsize=(10,5))
    ax1.imshow(image,cmap='gray')
    ax2.imshow(equalize,cmap='gray')
    plt.show()
    return ''


if __name__ == '__main__':
    run_main()
