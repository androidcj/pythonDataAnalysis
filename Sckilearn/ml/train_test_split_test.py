#coding:utf-8
import numpy as np
from sklearn.model_selection import train_test_split
from dask.array.tests.test_array_core import test_size
from sklearn.decomposition.tests.test_nmf import random_state


def run_main():
    X = np.random.randint(0,100,(10,4))
    y = np.random.randint(0,3,10)
    y.sort()
    #print '样本'    
    #print  X
    #print '标签：',y
    
    X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=1/3.,random_state=7)
    print '训啦集' 
    print X_train 
    print y_train 
    
    print '测试集' 
    print X_test 
    print y_test 
    
    
    
    return ''

if __name__=='__main__':
    run_main()
    