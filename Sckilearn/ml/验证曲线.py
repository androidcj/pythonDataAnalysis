#coding:utf-8
from sklearn.model_selection import validation_curve
from sklearn.datasets import load_digits
from sklearn.svm import SVC
import matplotlib.pyplot as plt
import numpy as np
from bokeh.charts.attributes import color



def runMain():
    digitis = load_digits()
    X = digitis.data
    y =digitis.target
    param_range = np.logspace(-6.5,-2,10);
    print param_range
    
    train_scores,val_scores = validation_curve(SVC(), X, y, param_name='gamma', param_range=param_range, cv=5, scoring='accuracy')
    
    train_scores_mean = np.mean(train_scores, axis=1)
    val_scores_mean = np.mean(val_scores, axis=1)
    
    plt.plot(param_range,train_scores_mean,'o-',color='r',label = 'training')
    plt.plot(param_range,val_scores_mean,'*-',color='g',label = 'cross validate')
    plt.xlabel('gamma')
    plt.ylabel('accuracy')
    plt.legend(loc='best')
    plt.show()
    
    return ''


if __name__=='__main__':
    runMain()
