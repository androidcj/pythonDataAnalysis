# -*- coding: utf-8 -*- 
'''
Created on 2018年4月21日

@author: caojun
'''
import pandas as pd
from sklearn.model_selection import train_test_split
from DatingDataAnalysisBySklearn.dataTools import *
from DatingDataAnalysisBySklearn.ml_tools import *

# 是否处理非平衡数据
is_process_unbalanced_data = True

# 是否交叉验证
is_cv = True

# 是否进行特征选择
is_feat_select = True

def run_main():
    path = './data/DatingData.csv'
    data_df = pd.read_csv(path)
    
    data_df = data_drop_na(data_df)
    print(data_df.shape[0])
    pair_data, labels, features = get_pair_data(data_df)
    
    
       # 进行特征选择
    if is_feat_select:
        pair_data, selected_features = select_features(pair_data, labels, features)
    
    
    
    n_pos_samples = labels[labels == 1].shape[0]
    n_neg_samples = labels[labels == 0].shape[0]
    print('正样本数：%d',format(n_pos_samples))
    print('负样本数：%d',format(n_neg_samples))
    
    # 处理非平衡数据
    if is_process_unbalanced_data:
        pair_data, labels = balance_samples(pair_data, labels)
     
    #切分数据集
    X_train,X_test,Y_train,Y_test = train_test_split(pair_data,labels,test_size = 0.1)
    
    
    #模型训练
    model_type = 'logistic_regression'     #逻辑回归模型
    
    model_ml = train_model(X_train,Y_train,model_type)
    rf_model_predictios = model_ml.predict(X_test)
    print(rf_model_predictios) 
        
    return ''


if __name__ == '__main__':
    run_main()