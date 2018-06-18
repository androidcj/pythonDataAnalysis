#coding:utf-8
from sklearn import datasets
from sklearn import svm
from sklearn.metrics import accuracy_score
import cPickle as pickle
import numpy as np
def run_main():
  
  iris = datasets.load_iris()
  digits = datasets.load_digits()
  
  #print iris.data
 # print iris.data.shape
  
  #选择svm模型
  svm_classifier = svm.SVC(gamma=0.001, C=100.)
  
  #选择训练数据个数为100
  n_test = 100  
  train_X = digits.data[:-n_test, :]
  train_y = digits.target[:-n_test]
    
  test_X =   digits.data[-n_test:, :]
  y_ture = digits.target[-n_test:]

  #训练
  svm_classifier.fit(train_X,train_y)
  
  #得到预测数据集
  y_pred = svm_classifier.predict(test_X)
  
#  print '预测标签' , y_pred
#  print '真实标签' , y_ture
  
  #查看结果
#  print accuracy_score(y_ture,y_pred)
  
  #保存模型
 # with open('svm_model.pkl','w') as f:
#  pickle.dump(svm_classifier, f)
  loadModel()
  
  return ''
    
def loadModel():
    #引入刚刚保存的模型
    with open("svm_model.pkl","r") as f:
        model = pickle.load(f)
    digits = datasets.load_digits()
    
    random_sample_index = np.random.randint(0,1796,5)
    print random_sample_index
    random_sample = digits.data[random_sample_index,:]
    print random_sample
    
    random_targets = digits.target[random_sample_index]
    random_predict = model.predict(random_sample)
    print '预测：' , random_predict
    print '实际：' , random_targets
    
if __name__=='__main__':
    run_main()