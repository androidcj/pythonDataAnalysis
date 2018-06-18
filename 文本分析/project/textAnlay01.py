#coding:utf-8

'''

@author: win7
'''

import nltk
from nltk.corpus import brown # 需要下载brown语料库

def run_main():
   # print(brown.categories())
  # nltk.download() 
    #pass;
    
    #分词
    sentense = "Python is a widely used high-level programming language for general-purpose programming."  
    tokens = nltk.word_tokenize(sentense)
    print(tokens)
    
    
    
    
    #结巴分词
    
    

if __name__=='__main__':
    run_main()

