
# -*- coding: utf-8 -*- 
'''

@author: win7
'''

from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from bayes.nb_tools import NativeBayes, cal_acc
 

def run_main():
    n_feat = 100    # 特征个数
    X, y = make_classification(
        n_samples=400,
        n_features=n_feat,
        n_classes=2,
        random_state=5)
    
    
    X_train,X_test,y_train,y_test = train_test_split(X,y,test_size = 0.3,random_state = 17)
    nb_model = NativeBayes(n_feat)
    # 样本特征为连续值，假设其符合高斯分布，则需要求出每个特征的均值和标准差
    # 这里称为统计参数 stats

    # 获取训练集中每个类别的统计参数
    tr_cls_stats = nb_model.get_cls_stats(X_train, y_train)
    for cls, samples_stats in tr_cls_stats.items():
         print('类%s的统计参数：'  %(cls))
         for i, feat_stats in enumerate(samples_stats):
            # 查看每个特征的统计参数
            print('第%i个特征的统计参数%s' %(i,feat_stats))
    # 根据训练样本的统计参数进行预测
    y_pred = nb_model.predict(tr_cls_stats, X_test)
    # 准确率
    print('准确率：%f' %(cal_acc(y_test, y_pred)))
if __name__ =='__main__':
    run_main()