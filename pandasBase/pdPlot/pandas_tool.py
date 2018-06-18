#coding:utf-8
import pandas as pd
import os

def inspect_dataset(df_data):
    print '数据集基本信息'
    print df_data.info()
    print '数据集有%i行.%i列' %(df_data.shape[0],df_data.shape[1])
    print '数据预览：'
    print df_data.head()