# -*- coding: utf-8 -*-
'''
Created on 2018.2.14

@author: win7
'''
import urllib2
import os

def def_main():
    path = "http://www.baidu.com"
    response = urllib2.urlopen(path)
  #  print type(response.read()) 
    text_file = 'E:\\urltext\\a.txt'
 #   os.mkdir(text_file)
    result = response.read()
    print result
    
    file_obj = open(text_file,'wb')
    file_obj.writelines(result)
    file_obj.close()
if __name__=='__main__':
    def_main()

