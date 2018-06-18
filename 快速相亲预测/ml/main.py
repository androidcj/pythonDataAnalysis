#coding:utf-8
from zip_tool import unZip

from pandas_tool import process_miss_data
import pandas as pd
from ml.pandas_tool import get_pair_data
from ml.ml_tools import selected_features, balance_samples, train_model,\
    print_test_results
from sklearn.model_selection._split import train_test_split
# from sklearn.decomposition.tests.test_nmf import random_state
import numpy as np

#是否处理非平衡数据  标志
is_process_unbalanced_data = True

#是否觉察言哼
is_cv = True


#是否进行特征选择
is_feat_select =True


#设置随即种子
random_seed = 7
np.random.seed(random_seed)


def runMain():
    dataset = '../dataset/Speed Dating Data.csv'
    dataframe = pd.read_csv(dataset)
    #print dataframe.shape;
        
    process_miss_data(dataframe)
    
    #对数据进行重构
    #获取重构的成对数据 ，以便放入预测模型
    pair_data,labels,features = get_pair_data(dataframe)
  
    #进行特征选择
    if is_feat_select:
        pair_data,selected_feature = selected_features(pair_data,labels,features)
        #pair_data, selected_features = select_features(pair_data, labels, features)
        print '旋转的特征：'
        print selected_feature
        
        
    n_pos_samples = labels[labels==1].shape[0]
    n_neg_samples = labels[labels==0].shape[0]   
    print '正样本数：%d' % n_pos_samples  
    print '负样本数：%d' % n_neg_samples
    
    
    #处理非平衡数据
    if is_process_unbalanced_data:
        pair_data,labels = balance_samples(pair_data,labels)
        
    print  'pair_data',  pair_data 
    #分割训练集和测试集
   # 分割训练集和测试集
    X_train, X_test, y_train, y_test = train_test_split(pair_data, labels, 
                                                        test_size=0.1, 
                                                        random_state=random_seed)
    #训练模型,测试模型
    print '逻辑回归模型'
    
    logistic_model = train_model(X_train,y_train,model_name='logistic_regression' ,is_cv = is_cv)
    logistic_model_predictions = logistic_model.predict(X_test)    #输出 0  1
    logistic_model_prob_predictions = logistic_model.predict_proba(X_test)   #输出概率
    
    #输出预测结果
    print_test_results(y_test,logistic_model_predictions,logistic_model_prob_predictions)
    
    
    print '支持向量机'
    svm_model= train_model(X_train, y_train, model_name='svm', is_cv=is_cv)
    svm_model_predictions = svm_model.predict(X_test)
    svm_model_prob_predictions = svm_model.predict_proba(X_test)
    #输出预测结果
    print_test_results(y_test,svm_model_predictions,svm_model_prob_predictions)
    
    print '随即僧林'
    rf_model = train_model(X_train, y_train, 
                           model_name='random_forest', is_cv=is_cv)
    rf_model_predictios = rf_model.predict(X_test)
    rf_model_prob_predictios = rf_model.predict_proba(X_test) 
    # 输出预测结果
    print_test_results(y_test, rf_model_predictios, rf_model_prob_predictios)
    
    
    #auc曲线描画
    
    
    
    return ''


if __name__=='__main__':
    runMain()
