#coding:utf-8
#回归模型
from sklearn import datasets

#线性回归模型
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split


def runMain():
    boston_data = datasets.load_boston()
    X =  boston_data.data
    y =  boston_data.target
  #  print '样本'
  #  print X[:5,:]
  #  print '标签'
  #  print y[:5]
    
    lr_model = LinearRegression()
    X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=1/3.,random_state=3)
    lr_model.fit(X_train, y_train)
    
    print 'xtrain====',X_train
    print 'X_test====',X_test
    
    print 'y_train====',y_train
    print 'y_test====',y_test
    #返回参数
    params  = lr_model.get_params()
    print '参数：'
    print params
    
    train_scor = lr_model.score(X_train,y_train)
    test_score = lr_model.score(X_test,y_test)
    print '训练集打分：'
    print train_scor
    print '测试集打分：'
    print test_score
    
    
    
    
    return ''


if __name__=='__main__':
    runMain()
