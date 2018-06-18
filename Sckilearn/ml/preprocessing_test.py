#coding:utf-8
#特征归一化
from sklearn import preprocessing
import numpy as np



#让数据更加聚集，可提高数据预测准确性

def run_main():
    x1 = np.random.randint(0,1000,5).reshape(5,1)
    x2 = np.random.randint(0,10,5).reshape(5,1)
    x3 = np.random.randint(0,100000,5).reshape(5,1)
    
    X = np.concatenate([x1,x2,x3],axis = 1)
    print X
    
    print preprocessing.scale(X)
    
    
    return ''

if __name__=='__main__':
    run_main()