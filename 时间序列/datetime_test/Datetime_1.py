#coding:utf-8
'''


@author: win7
'''
import pandas as pd
from datetime import datetime

def main_func():
    now = datetime.now()
    
    print "年:%i,月:%i,日:%i" %(now.year,now.month,now.day)

    diff = datetime(2017,3,4,17) - datetime(2017,2,18,15)
    print diff
    
    print "经历了%s天  ,%s秒    " %(diff.days,diff.seconds)
    
    obj1 = pd.Series(['1983-01-12','1985/05/11','1986-07-11'],index=['year1','year2','year3'])
    obj2 = pd.to_datetime(obj1)
    print obj1[['year1','year3']]
    print obj2[0:2]
    
if __name__ == "__main__":
    main_func()