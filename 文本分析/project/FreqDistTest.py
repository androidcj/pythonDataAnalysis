# -*- coding: utf-8 -*- 

'''
Created on 2018年2月20日

@author: win7
'''

import nltk
from nltk import FreqDist

def run_main():
    
    text1 = 'I like the movie so much '
    text2 = 'That is a good movie '
    text3 = 'This is a great one '
    text4 = 'That is a really bad movie '
    text5 = 'This is a terrible movie'
    
    text = text1+text2+text3+text4+text5
    
    #分词
    word_token = nltk.word_tokenize(text)
    freq_disk = FreqDist(word_token)
    
    print(freq_disk['is'])
    
    
    #取出常用的单词
    n = 5
    most_words = freq_disk.most_common(n)
    print(most_words)
    
    rre = lookup_pos(most_words)
    print(rre)
    
    
    new_text = 'That one is a good movie. This is so good!'
    
    
    res1 = [0]*n
    new_words = nltk.word_tokenize(new_text)
    for nw in new_words:
        if nw in rre.keys():
            res1[rre[nw]] = res1[rre[nw]]+1
    
    
    print(res1)
    

def lookup_pos(most_common_words):
    result = {}
    pos = 0
    for bean in most_common_words:
        result[bean[0]] = pos
        pos=pos+1
    return result
    
    


if __name__ =='__main__':
    run_main()