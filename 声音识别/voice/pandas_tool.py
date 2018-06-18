#coding:utf-8
'''
Created on 

@author: win7
'''


import seaborn as sns
import matplotlib.pyplot as plt
def insect_dataset(file_df):
    file_df.info()
    return ''

  
def drop_na(file_df):
    if file_df.isnull().values.any():
        file_df = file_df.fillna(0.)
    
    return file_df.reset_index()   


#特征分布可视化
def visaulize_two_feature(file_df,col_label1,col_label2):
    g = sns.FacetGrid(file_df,hue='label',size=8)
    g = g.map(plt.scatter,col_label1,col_label2)
    g.add_legend()
    plt.show()
    return ''
     
     
     
def visaulize_single_feature(file_df,col_label1):     
    sns.boxplot(x="label",y="col_label1",data = file_df)
    g2  =sns.FacetGrid(file_df,hue='label',size = 6)
    g2.map(plt.scatter,col_label1)
    g2.add_legend()
    plt.show()
    return ''

def visaulize_muilt_feature(file_df,fea_name):
    sns.PairGrid(file_df[fea_name],hue='label',size=2)
    plt.show()
    return ''