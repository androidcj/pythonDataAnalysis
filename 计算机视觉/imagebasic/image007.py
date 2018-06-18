#coding:utf-8
'''
颜色特征提取与sift特征   hog特征
@author: win7
'''
from skimage import data,img_as_float,exposure
from skimage.feature import daisy
from matplotlib import pyplot as plt
from skimage.feature import hog



def run_main():
    camera = img_as_float(data.camera())
#     hist,bin_centers = exposure.histogram(camera, nbins=10)
#     print(hist)
#     print(bin_centers)
    #sift特征
#     daisy_feat,daisy_img = daisy(camera, step=180, radius=58, rings=2, histograms=6,  visualize=True)
#     print(daisy_feat.shape)
#     plt.imshow(daisy_img)
#     plt.show()
    
    #hog特征
    hog_feat,hog_img = hog(camera,visualise=True)
    print(hog_feat.shape)
    plt.imshow(hog_img)
    plt.show()
    return ''
    
    

if __name__ == '__main__':
    run_main()