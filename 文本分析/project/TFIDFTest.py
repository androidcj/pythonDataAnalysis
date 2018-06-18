# -*- coding: utf-8 -*- 
'''
@author: win7
'''
import nltk
from nltk.text import TextCollection

def run_main():
    text1 = 'I like the movie so much '
    text2 = 'That is a good movie '
    text3 = 'This is a great one '
    text4 = 'That is a really bad movie '
    text5 = 'This is a terrible movie'
    
    tf_analy= TextCollection([text1,text2,text3,text4,text5])
    
    new_text = 'That one is a good movie. This is so good!'
    word = 'That' 
    tf_idf_val = tf_analy.tf_idf(word, new_text)
    print(tf_idf_val)

if __name__ =='__main__':
    run_main()

