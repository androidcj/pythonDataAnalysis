#coding:utf-8
'''
Created on 2018年2月18日

@author: win7
'''
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def run_main():
    ser_obj1 = pd.Series(np.random.randn(1000),index=pd.date_range('2017-01-01',periods=1000))
    
   
    ser_obj1 = ser_obj1.cumsum()
    print ser_obj1.head(10)
    
    r_obj = ser_obj1.rolling(window=5)
    print r_obj.mean()
    
    plt.figure(figsize=(15, 5))
    ser_obj1.plot(style='r--')
    ser_obj1.rolling(window=10,center=True).mean().plot(style='b')
    plt.show()
if __name__=='__main__':
    run_main()


