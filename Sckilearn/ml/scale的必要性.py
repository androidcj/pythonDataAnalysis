#coding:utf-8
#scala的重要性
from sklearn.datasets import make_classification
from sklearn import svm, preprocessing
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
def run_main():
    
    
    X,y = make_classification(n_samples=300,n_features=2,n_redundant=0,n_informative=2,random_state=25,n_clusters_per_class=1,scale=100)
    plt.scatter(X[:,0],X[:,1],c=y)
  #  plt.show()
    
    X = preprocessing.scale(X)
    X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=1/3.,random_state=7)
    svm_classfier = svm.SVC()
    svm_classfier.fit(X_train,y_train)
    scor =svm_classfier.score(X_test,y_test)
    print scor
    return ''


if __name__=='__main__':
    run_main()