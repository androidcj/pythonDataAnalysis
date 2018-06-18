#coding:utf-8
import numpy as np
import operator

#得到分类器的正确率

def c(n,k):
    return reduce(operator.mul, range(n-k+1,n+1))/reduce(operator.mul,range(1,k+1))

def bagging(n,p):
    s=0
    for i in range(n/2+1,n+1):
        s+=c(n,i)*p**i*(1-p)**(n-i)
    return s

if __name__ =="__main__":
    for i in range(9,100,10):
        print i,'次才养的正确率为:',bagging(i,0.6)
    

