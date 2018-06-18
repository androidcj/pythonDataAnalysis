#coding:utf-8

'''
Created on 2017  

@author: caojun 
'''
import pandas as pd
from pandas_tool import insect_dataset,drop_na,visaulize_two_feature,visaulize_single_feature,visaulize_muilt_feature
from mistune import inspect
from sklearn import preprocessing
from sklearn.model_selection._split import train_test_split
from dask.array.tests.test_array_core import test_size
from sklearn.decomposition.tests.test_nmf import random_state
from sklearn.neighbors.classification import KNeighborsClassifier
from sklearn.cross_validation import cross_val_score
import numpy as np  
from sklearn import svm
  
  
  
  
def run_main():
    
    file_df = pd.read_csv('../dataset/voice.csv')
 #   print file_df
    insect_dataset(file_df)
    #填充空数据
    drop_na(file_df)
    #查看label的个数    分组显示
 #   print file_df['label'].value_counts()
    #特征分布可视化
    fea_name1 = 'meanfun'
    fea_name2 = 'centroid'
    
    #两个属性的特征图
   # visaulize_two_feature(file_df,fea_name1,fea_name2)
    
    #艺术性属性的特征图
   # visaulize_single_feature(file_df,fea_name1)
    
    
    #多个特征
    fea_name=['meanfreq','Q25','Q75','skew','centroid','label']
   # visaulize_muilt_feature(file_df,fea_name)
    
    X = file_df.iloc[:,:-1].values
    file_df['label'].replace('male',0,inplace=True)
    file_df['label'].replace('female',1,inplace=True)
    y = file_df['label'].values
    
    
    #特征归一化
    X= preprocessing.scale(X)
    
    
    #分割训练集，测试集
    X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=1/3.,random_state=5)
    
    
    #选择模型  交叉验证
    cv_scores =[]
    k_range = range(1,31)
    for k in k_range:
        knn = KNeighborsClassifier(k)
      #  print 'knn:',knn
        scores = cross_val_score(knn,X_train,y_train,cv=10,scoring='accuracy')
        score_mean = scores.mean()
        cv_scores.append(score_mean)
        print '%i:%.4f' %(k,score_mean)
    
    best_k = np.argmax(cv_scores)+1
    
    #训练模型
    knn_model= KNeighborsClassifier(best_k)
    knn_model.fit(X_train, y_train)
    print '测试模型，准确率：',knn_model.score(X_test,y_test)
    
    return ''

if __name__=='__main__':
    run_main()
