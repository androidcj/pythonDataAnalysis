#coding:utf-8
'''
增强对比度
@author: win7
'''
from skimage import data
from skimage import exposure
from matplotlib import pyplot as plt


def run_main():
    image = data.camera()
    hist,bin_centers = exposure.histogram(image)
    
    #改变对比度   image中小于10的像素值设为0  大于180的像素值设为255
    high_constract = exposure.rescale_intensity(image,in_range=(10,180))
    
    hist2,bin_centers2 = exposure.histogram(high_constract)
    fig,(ax_1,ax_2) = plt.subplots(ncols=2,figsize=(10,5))
    ax_1.imshow(image,cmap = 'gray')
    ax_2.imshow(high_constract,cmap = 'gray')
    
    
    fig,(ax_hist1,ax_hist2) = plt.subplots(ncols=2,figsize=(10,5))
    ax_hist1.fill_between(bin_centers,hist)
    ax_hist2.fill_between(bin_centers2,hist2)
    
    plt.show()
    
    
    return ''
    


if __name__ == '__main__':
    run_main()
