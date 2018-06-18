#coding:utf-8

'''

@author: win7
'''
import nltk
from nltk.corpus import stopwords
def run_main():
    
    words = nltk.word_tokenize('Python is a widely used programming language.')
    filtered_words = [word for word in words if word not in stopwords.words('english')]
    print('原始词：', words)
    print('去除停用词后：', filtered_words)


if __name__=='__main__':
    run_main()
