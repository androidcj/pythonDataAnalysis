#coding:utf-8
from sklearn import datasets
from sklearn.model_selection._validation import learning_curve
from sklearn.svm import SVC
import numpy as np
import matplotlib.pyplot as plt
def runMain():
    digits= datasets.load_digits()
    X = digits.data
    y = digits.target
    #gamma = 0.001
    train_sizes,train_scores,val_scores = learning_curve(SVC(gamma=0.001),X,y,cv=10,scoring='accuracy',train_sizes=[0.1,0.25,0.5,0.75,1])
    train_scores_mean = np.mean(train_scores, axis=1)
    val_scores_mean = np.mean(val_scores,axis=1)
    print train_sizes
    plt.plot(train_sizes,train_scores_mean,'-o',color='r',label = 'trains')
    plt.plot(train_sizes,val_scores_mean,'*-',color='g',label = 'cross validate')
    plt.xlabel('train_simple_size')
    plt.ylabel('accuracy')
    plt.legend(loc='best')
    plt.show()
    
    return ''


if __name__ == '__main__':
    runMain()
