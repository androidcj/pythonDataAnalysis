#coding:utf-8

'''
中值滤波
@author: win7
'''

from skimage import data
from skimage import exposure
from skimage.filters.rank import median
from skimage.morphology import disk 
from matplotlib import pyplot as plt

def run_main():
    
    img = data.camera()
    med1 = median(img, disk(3))
    med2 = median(img, disk(5))
    fig,(ax1,ax2,ax3) = plt.subplots(ncols=3, figsize=(10,5))
    ax1.imshow(img,cmap='gray');
    
    ax2.imshow(med1,cmap='gray');
    
    ax3.imshow(med2,cmap='gray');
    plt.show()
    
    
    return '';


if __name__ == '__main__':
    run_main()