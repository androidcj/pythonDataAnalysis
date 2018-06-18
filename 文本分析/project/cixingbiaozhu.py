# -*- coding: utf-8 -*- 
'''

@author: win7
'''
import nltk

def run_main():
 #   nltk.download()
    words = nltk.word_tokenize('Python is a widely used programming language.')
    print(nltk.pos_tag(words))
    

if __name__=='__main__':
    run_main()