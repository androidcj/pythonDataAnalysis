
#coding:utf-8
'''
Created on 2018年4月5日

@author: win7
'''

import skimage
import numpy  as np
from matplotlib import pyplot as plt


def run_main():
    
    #随机生成500*500的多维数组
    random_vec = np.random.random((500,500))
#     random_vec  = np.array([500,500,500])
#     random_vec = np.expand_dims(random_vec, axis=0) 
    plt.imshow(random_vec,cmap='gray')
#     plt.colorbar()
    plt.show()
    
    return '';
    


if __name__ == '__main__':
    run_main()
