# -*- coding: utf-8 -*- 

'''
@author: win7
'''
from nltk.stem.porter import PorterStemmer
from nltk.stem import SnowballStemmer
from nltk.stem.lancaster import LancasterStemmer

def run_main():
    post_stemming =  PorterStemmer()
    print(post_stemming.stem("looking"))
    print(post_stemming.stem("looked"))
    
    
    snow_stem = SnowballStemmer('english')
    print(snow_stem.stem("looking"))
    print(snow_stem.stem("looked"))
    
    
    lancaster = LancasterStemmer()
    
    print(lancaster.stem("looking"))
    print(lancaster.stem("looked"))
if __name__=='__main__':
    run_main()