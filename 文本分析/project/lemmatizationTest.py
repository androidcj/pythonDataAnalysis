
# -*- coding: utf-8 -*- 
'''

@author: win7
'''

import nltk
from nltk.stem import WordNetLemmatizer
def run_main():
  #  nltk.download() 
   #词形归并
   netlem = WordNetLemmatizer();
   #定义词性    pos=v表示是动词
   print(netlem.lemmatize("went", pos="v")) 
   print(netlem.lemmatize("are"))
   
   

if __name__=='__main__':
    run_main()
