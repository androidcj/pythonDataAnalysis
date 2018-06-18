#coding:utf-8
import numpy as np
import datetime
import matplotlib.pyplot as plt
import pandas as pd

def run_main():
     filename = 'E:/python/lecture02_codes/codes/presidential_polls.csv'
     with open(filename,'r') as f:
         name_index_lst = f.readline()[:-1]
         print name_index_lst
         col_names_lst = name_index_lst.split(',')   
         
         use_col_name_lst = ['enddate','rawpoll_clinton','rawpoll_trump','adjpoll_clinton','adjpoll_trump']
         user_name_index = [col_names_lst.index(username) for username in use_col_name_lst]   
         print user_name_index 
         user_name_list = pd.read_csv(filename, dtype=str,parse_dates=["enddate"],names=use_col_name_lst,usecols=use_col_name_lst)
#      print  user_name_list   
         print ("user_name_list=",user_name_list)
         date_row = user_name_list['enddate']
         date_arr = np.array(date_row)
         date_arr = np.unique(date_arr)
         print date_arr
     
     
    
if __name__ == '__main__':
    run_main()