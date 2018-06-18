# -*- coding: utf-8 -*- 
'''
Created on 2018年4月21日

@author: win7
'''
from sklearn import linear_model, svm
from sklearn.ensemble.forest import RandomForestClassifier
from sklearn.metrics.ranking import roc_curve, auc, roc_auc_score
import matplotlib.pyplot as plt
from sklearn.metrics.classification import accuracy_score
import numpy as np
from sklearn.model_selection._search import GridSearchCV
from sklearn.feature_selection.variance_threshold import VarianceThreshold
from sklearn.feature_selection.univariate_selection import SelectPercentile
import pandas as pd


def select_features(pair_data, labels, features):
    # 1. 过滤掉“低方差”的特征列
    vt_sel = VarianceThreshold(threshold=(0.9*(1-0.9)))
    vt_sel.fit(pair_data)
#     print(vt_sel.get_support())
    
 
    #过滤掉噪声特征
    features = features[vt_sel.get_support()]
    
    pair_data = pair_data[:,vt_sel.get_support()]
#     print(pair_data)
    #得到最重要的95%的样本
    sp_sel = SelectPercentile(percentile=95)
    sp_sel.fit(pair_data, labels)
    features = features[sp_sel.get_support()]
    pair_data_1 = pair_data[:,sp_sel.get_support()]
#     print(pair_data_1)
    return pair_data_1,features



def balance_samples(pair_data, labels):
    labels = labels.reshape((labels.size, 1))
    all_data = np.concatenate((pair_data, labels), axis=1)
    pos_data = all_data[all_data[:,-1]==1]     #match的数据
    neg_data = all_data[all_data[:,-1]==0]     #nomatch的数据
    n_pos_samples = pos_data.shape[0]
    
    #  目前负样本数远超正样本数
    n_neg_data_num = int(n_pos_samples*2)
    sampled_neg_data = neg_data[np.random.choice(neg_data.shape[0],n_neg_data_num)]
    sampled_all_data = np.concatenate((sampled_neg_data,pos_data))
    selected_pair_data = sampled_all_data[:,:-1]
    selected_labels = sampled_all_data[:,-1]
    return selected_pair_data,selected_labels




def train_model(X_train,Y_train,model_type):
    
    if model_type == 'logistic_regression':
        lr_model = linear_model.LogisticRegression()
        #参数交叉验证
       
        params = {'C':np.logspace(1e-4, 1, 10)}
        gs_model = GridSearchCV(lr_model, param_grid=params, cv=5, 
                                    scoring='roc_auc', verbose=3)
        print(Y_train)
        gs_model.fit(X_train,Y_train.astype('int'))
        #得到最优模型
        best_model = gs_model.best_estimator_
        
    
    elif model_type == 'svm':
        #如果使用svm来训练模型
        svm_model = svm.SVC(probability=True)
        params = {'C': [0.1, 1, 10, 100, 1000],
                      'gamma': [1e-5, 1e-4, 1e-3, 1e-2, 0.1]}
    
        gs_model = GridSearchCV(svm_model, param_grid=params, cv=5, 
                                    scoring='roc_auc', verbose=3)
        
        gs_model.fit(X_train,Y_train)
        best_model = gs_model.best_estimator_
        
    elif model_type == 'random_forest':    
        #随机森林
        rf_model= RandomForestClassifier()
        params = {'n_estimators': [20, 40, 60, 80, 100]}
        gs_model = GridSearchCV(rf_model, param_grid=params, cv=5, 
                                    scoring='roc_auc', verbose=3)
        
        gs_model.fit(X_train, Y_train)
        best_model = gs_model.best_estimator_
        
        
        
    return best_model
        
        
        