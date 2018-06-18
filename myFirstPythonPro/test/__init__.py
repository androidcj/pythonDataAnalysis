
#coding:utf-8
x_2_lst = [x**2 for x in range(10)]
#print x_2_lst

name_lst = ['poNNY MA', 'rObIN li', 'steve JOBS', 'bILL gates']
standard_name_lst = map(str.title, name_lst)
#print standard_name_lst



number_lst = range(-10, 10)
filtered_lst = filter(lambda x : x<0, number_lst)
#print number_lst
#print filtered_lst


import numpy as np

# 生成指定维度的随机多维数据
data = np.random.rand(2, 3)
#print data
#print type(data)


filename = 'E:/python/lecture02_codes/codes/presidential_polls.csv'
data_arr = np.loadtxt(
    filename,
    delimiter=',',
    dtype=str,
    usecols=(0,2,3)
    )

#print data_arr,data_arr.shape

import scipy as sp
from scipy import stats
import matplotlib.pyplot as plt
fig = plt.figure()
#random_arr = np.random.randn(100)
#plt.plot(random_arr)

#ax1 = fig.add_subplot(2,2,1)
#ax2 = fig.add_subplot(2,2,2)
#ax3 = fig.add_subplot(2,2,3)
#ax4 = fig.add_subplot(2,2,4)

#plt.plot(random_arr)
#plt.show()

#直方图
#plt.hist(np.random.randn(100),bins=10,color='b',alpha=0.3)
#plt.show()

#散点图
#x=np.arange(50)
#y=x+5 * np.random.randn(50)
#plt.scatter(x,y)
#plt.show()

#柱状图
#x=np.arange(5)
#y1,y2 = np.random.randint(1,25,size=(2,5))
#width=0.25
#ax=plt.subplot(1,1,1)
#ax.bar(x,y1,width,color='r')
#ax.bar(x+width,y2,width,color='g')
#ax.set_xticks(x+width)
#ax.set_xticklabels(['a','b','c','d','e'])
#plt.show()


#矩阵绘图

#m = np.random.rand(10,10)
#print m
#plt.imshow(m, interpolation='nearest', cmap=plt.cm.ocean)
#plt.colorbar()
#plt.show()

#在分块页面中显示
fig,subplot_arr = plt.subplots(2,2)
subplot_arr[0,0].hist(np.random.randn(100),bins=10,color='b',alpha=0.3)
plt.show()









