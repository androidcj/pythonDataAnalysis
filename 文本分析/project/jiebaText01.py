# -*- coding: utf-8 -*- 

'''

@author: win7
'''


import sys



import nltk
import jieba

def run_main():

    
    seg_list = jieba.cut("欢迎来到小象学院",cut_all=True)
    print(u"全模式: " + "/ ".join(seg_list))  # 全模式
    
    seg_list1 =  jieba.cut("欢迎来到小象学院",cut_all=False)
    print(u"精准模式: " + "/ ".join(seg_list1))  # 精准模式
    
    

if __name__=='__main__':
    run_main()

