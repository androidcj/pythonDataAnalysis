
# -*- coding: utf-8 -*- 
'''

@author: win7
'''
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer




def run_main():
    raw_text = 'Life is like a box of chocolates. You never know what you\'re gonna get.'
    word_token = nltk.word_tokenize(raw_text)
    
    #停用词
    wordstext = [word for word in word_token if word not in stopwords.words('english')]
    #print(wordstext)
    
    
    pos_tags = nltk.pos_tag(wordstext)
    print(pos_tags)
    
    word_res = [stem_method(word[0]) for word in pos_tags]
    
    print(word_res)
    
    #for pp in pos_tags:
    #    print(pp[0])


def stem_method(p):
    wordstem = WordNetLemmatizer()
    return wordstem.lemmatize(p)
    
if __name__ =='__main__':
    run_main()