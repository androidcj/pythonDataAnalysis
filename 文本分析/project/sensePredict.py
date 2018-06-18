# -*- coding: utf-8 -*- 

'''

@author: win7
'''

import nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from nltk.classify import NaiveBayesClassifier

def run_main():
    text1 = 'I like the movie so much!'
    text2 = 'That is a good movie.'
    text3 = 'This is a great one.'
    text4 = 'That is a really bad movie.'
    text5 = 'This is a terrible movie.'
    
    
    #构建训练数据
    
    train_data = [[re_work_process(text1),1],
                  [re_work_process(text2),1],
                  [re_work_process(text3),1],
                  [re_work_process(text4),0],
                  [re_work_process(text5),0]
                  ]
    #得到训练之后的模型
    nb_model = NaiveBayesClassifier.train(train_data)
    
    #测试数据
    text6 = 'That is a very great one.'
    
    print(nb_model.classify(re_work_process(text6)))
    
    
    
    


def re_work_process(text):
    word_token = nltk.word_tokenize(text)
    
    wordLem = WordNetLemmatizer()
    
    
    #归一化
    lemword = [wordLem.lemmatize(word) for word in word_token]
    
    
    #去除停用词
    
    word_res = [word for word in lemword if word not in stopwords.words('english')]
    
    return {word:True for word in word_res }
    
    
    


if __name__=='__main__':
    run_main()
