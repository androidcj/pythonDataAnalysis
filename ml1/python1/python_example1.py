#coding:utf-8

'''
@author: win7
'''

import numpy as np
import matplotlib
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import time
from scipy.optimize import leastsq
import scipy.optimize as opt
import scipy
import matplotlib.pyplot as plt
from scipy.stats import norm, poisson
from scipy.interpolate import BarycentricInterpolator
from scipy.interpolate import CubicSpline
import math


def run_main():
    
#     a = np.arange(0,60,10).reshape(-1,1)+np.arange(6)
#     print a
    
#     endpoint=False 表示不包含末位置
#     c = np.linspace(1, 10, 10, endpoint=False)
#     print c
    
    
#     d = np.logspace(1, 2, 10, endpoint=True)
#     print d
    t = np.linspace(0,7,100)
    x = 16* np.sin(t) ** 3
    y = 13 * np.cos(t) -5*np.cos(2*t) - 2*np.cos(3*t) -np.cos(4*t)
    plt.plot(x,y,'r-',linewidth=2)
    plt.grid(True)
    plt.show()
      


    return

if __name__ == '__main__':
    run_main()