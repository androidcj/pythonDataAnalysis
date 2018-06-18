#coding:utf-8
from sklearn.feature_selection.variance_threshold import VarianceThreshold
from sklearn.feature_selection.univariate_selection import SelectPercentile
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn import linear_model, svm
from sklearn.model_selection._search import GridSearchCV
from sklearn.metrics.classification import accuracy_score
from sklearn.metrics.ranking import roc_auc_score, roc_curve, auc
from sklearn.ensemble.forest import RandomForestClassifier


#提取主要特征
def selected_features(pair_data,labels,features):
    #过滤掉低方差的特征值
    vt_sel = VarianceThreshold(threshold=(0.85*(1-0.85)))
    vt_sel.fit(pair_data)
    
    #本次试验中没有需要过滤的特征，在这里只是举例
    
    print 'vt_sel.get_support()====',vt_sel.get_support()
    sel_features1 = features[vt_sel.get_support()]
    
    
    sel_pair_data1 = pair_data[:,vt_sel.get_support()]
    print '低方差过滤掉%d个特征' %(features.shape[0] - sel_features1.shape[0])
    
    print 'features.shape[0]====',features.shape[0],'======',features.shape
    print 'sel_features1.shape[0]====',sel_features1.shape[0],'=========',sel_features1.shape
    
    
    #2  根据  单变量统计分析   选择特证
    #保留重要的前90%的特征
    sp_sel = SelectPercentile(percentile=95)
    sp_sel.fit(sel_pair_data1,labels)
    
    sel_features2 = sel_features1[sp_sel.get_support()]
    
    sel_pair_data2 = sel_pair_data1[:,sp_sel.get_support()]
    print '单变量统计分析过滤掉%d个特征' %(sel_features1.shape[0] - sel_features2.shape[0])
    
    
    # 根据特征scroe绘制柱状图
    feat_ser = pd.Series(data=sp_sel.scores_,index=features) 
    sort_feat_ser = feat_ser.sort_values(ascending=False)
    plt.figure(figsize=(18,12))
    sort_feat_ser.plot(kind='bar')
    plt.savefig('../feat_importance.png')
    plt.show()
    return sel_pair_data2,sel_features2

#平衡数据
def balance_samples(pair_data,labels):
    labels = labels.reshape((labels.size, 1))
    all_data = np.concatenate((pair_data,labels),axis=1)
    
    pos_data = all_data[all_data[:,-1]==1]      #此处得到的负样本过多余正样本
    neg_data = all_data[all_data[:,-1]==0]
    n_pos_samples = pos_data.shape[0]
    #已知负样本是过多
    n_selected_neg_samples = int(n_pos_samples*2)
    sampled_neg_data = neg_data[np.random.choice(neg_data.shape[0],n_selected_neg_samples)]
    print 'sampled_neg_data====',sampled_neg_data.shape
    print 'pos_data====',pos_data.shape
    sample_all_data = np.concatenate((sampled_neg_data,pos_data))
    selected_pair_data = sample_all_data[:,:-1]
    selected_labels = sample_all_data[:,-1]
    return selected_pair_data,selected_labels

def train_model(X_train,y_train,model_name='logistic_regression',is_cv=False):
    
    #训练分类模型  默认不采用交叉验证
    if model_name=='logistic_regression':
        #逻辑回归
        lr_model = linear_model.LogisticRegression()
        if is_cv:
            #交叉验证
            params = {'C':[1e-4,1e-3,1e-2,0.1,1]}
            gs_model = GridSearchCV(lr_model,param_grid=params,cv=5,scoring='roc_auc',verbose=3)
            print 'X_train===',X_train.shape
            print 'y_train===',y_train.shape
            #gs_model.transform(X_train)
            gs_model.fit(X_train,y_train)
            print '最优的参数：',gs_model.best_params_
            best_model = gs_model.best_estimator_
       
        else :
            print '使用模型默认参数'   
            lr_model.fit(X_train, y_train)
            best_model = lr_model
    if model_name=='svm':
        svm_model = svm.SVC(probability=True)
        if is_cv:
            print '交叉验证的结果是======='
            params = {'C':[0.1,1,10,100,1000],
                      'gamma':[1e-5,1e-4,1e-3,1e-2,0,1],}
            gs_model = GridSearchCV(svm_model,param_grid=params,cv=5,scoring='roc_auc',verbose=3)
            gs_model.fit(X_train,y_train)
            print '最优参数：',gs_model.best_params_
            best_model = gs_model.best_estimator_
    
    
    if model_name == 'random_forest':
        # 随机森林
        rf_model = RandomForestClassifier()
        if is_cv:
            print '交叉验证'
            params = {'n_estimators': [20, 40, 60, 80, 100]}
            gs_model = GridSearchCV(rf_model,param_grid=params,cv=5,scoring='roc_auc',verbose=3)
            gs_model.fit(X_train, y_train)
            print '最优参数:', gs_model.best_params_
            best_model = gs_model.best_estimator_
            
                
    return best_model

def print_test_results(true_labels, pred_labels, pred_probs):
    """
            输出预测结果，包括准确率和AUC值
    """
    print '预测准确率：%.2f' % accuracy_score(true_labels, pred_labels)
    print '预测AUC值：%.4f' % roc_auc_score(true_labels, pred_probs[:, 1])
    print ''
    

       #  根据预测值和真实值绘制ROC曲线
def plot_roc(true_labels,pred_probs,fig_title='',savepath=''):
    
    false_positive_rate,true_positive_rate, _ =roc_curve(true_labels,pred_probs[:, 1], pos_label=1)
    roc_auc = auc(false_positive_rate,true_positive_rate)
    plt.figure()
    plt.title(fig_title)
    plt.plot(false_positive_rate,true_positive_rate,'b',label='AUC = %0.4f'% roc_auc)
    plt.plot([0,1],[0,1],'r--')
    plt.legend(loc='lower right')
    plt.ylabel('True Positive Rate')
    plt.xlabel('False Positive Rate')
    if savepath != '':
        plt.savefig(savepath)
    plt.show()
    
    
    return ''
