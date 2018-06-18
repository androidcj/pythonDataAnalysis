#coding:utf-8
#交叉验证
from sklearn import datasets
from sklearn.model_selection import train_test_split,cross_val_score
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt
from sklearn.decomposition.tests.test_nmf import random_state


def run_main():
    iris = datasets.load_iris();
    X = iris.data;
    y = iris.target;
    X_train,X_test,y_train,y_test = train_test_split(X,y,test_size = 1/3.,random_state=5)
    k_range = range(1,31)
    cv_scross=[]
    for n in k_range:
        knn = KNeighborsClassifier(n)
        scross = cross_val_score(knn,X_train,y_train,cv=10,scoring='accuracy')    #分类问题
        #print scross
       # scross = cross_val_score(knn,X_train,y_train,cv=10,scoring='neg_mean_squared_error')    #回归问题
        cv_scross.append(scross.mean())
    
#    plt.plot(k_range,cv_scross) 
#    plt.xlabel('K')
#    plt.ylabel('Accuracy')
#    plt.show()
#可以从途中看到  最优解为15

     #选择最优解
    beat_knn = KNeighborsClassifier(15)
    beat_knn.fit(X_train,y_train)
    scres = beat_knn.score(X_test, y_test)
    print '得到的分数是：'
    print scres
    
    pn=beat_knn.predict(X_test)
    print '得到的预测结果：'
    print pn
    return ''



if __name__=='__main__':
    run_main()
