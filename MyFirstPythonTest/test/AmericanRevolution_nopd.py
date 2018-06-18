#coding:utf-8
import numpy as np
import datetime
import matplotlib.pyplot as plt
import pandas as pd


def check_is_float(s):
    try:
        float(s)
    except: 
        return False
    return True        
def format_time(datetimes):
    dtime = datetime.datetime.strptime(datetimes,'%m/%d/%Y')
    dtimestr = dtime.strftime('%Y-%m')
#     print ("dtimestr",dtimestr)
    return dtimestr

def get_sum(data_lst):
    data1 = filter(check_is_float,data_lst)
    data_arr = np.array(data1,np.float)
    data_sum = np.sum(data_arr)
    return data_sum
    
    
def run_main():
     filename = 'E:/python/lecture02_codes/codes/presidential_polls.csv'
     with open(filename,'r') as f:
         name_index_lst = f.readline()[:-1]
         col_names_lst = name_index_lst.split(',')   
         use_col_name_lst = ['enddate','rawpoll_clinton','rawpoll_trump','adjpoll_clinton','adjpoll_trump']
         user_name_index = [col_names_lst.index(username) for username in use_col_name_lst]   
         
         data_arr = np.loadtxt(
             filename,
             skiprows=1,
             delimiter=',',
             dtype=str,
             usecols = user_name_index
             )
         
         
         date_lst = data_arr[:,0]
         date_lst = date_lst.tolist()
#          print("date_lst",date_lst)    #得到时间
         date_lst1 = map(format_time,date_lst)
#          print date_lst1
         date_array = np.array(date_lst1)
         datetime_array = np.unique(date_array)
         datetime_array = np.sort(datetime_array)
#          print date_array
         
#          rawpoll_clinton_data =  data_arr[:,use_col_name_lst.index('rawpoll_clinton')]
         
         rawpoll_clinton_data =  data_arr[:,use_col_name_lst.index('rawpoll_clinton')]
         rawpoll_trump_data =  data_arr[:,use_col_name_lst.index('rawpoll_trump')]
         adjpoll_clinton_data =  data_arr[:,use_col_name_lst.index('adjpoll_clinton')]
         adjpoll_trump_data =  data_arr[:,use_col_name_lst.index('adjpoll_trump')]
         #遍历时间  得到
         result=[]
         for endtime in datetime_array:
             
            rawpoll_clinton_month_data = rawpoll_clinton_data[date_array == endtime]
            rawpoll_trump_month_data = rawpoll_trump_data[date_array == endtime]
            adjpoll_clinton_month_data = adjpoll_clinton_data[date_array == endtime]
            adjpoll_trump_month_data = adjpoll_trump_data[date_array == endtime]
            
            
#             print ("month",endtime,"rawpoll_clinton_month_data",rawpoll_clinton_month_data)
            rawpoll_clinton_month_data_sum = get_sum(rawpoll_clinton_month_data) 
            rawpoll_trump_month_data_sum = get_sum(rawpoll_trump_month_data) 
            adjpoll_clinton_month_data_sum = get_sum(adjpoll_clinton_month_data) 
            adjpoll_trump_month_data_sum = get_sum(adjpoll_trump_month_data) 
            result.append((endtime,rawpoll_clinton_month_data_sum,rawpoll_trump_month_data_sum
                          ,adjpoll_clinton_month_data_sum,adjpoll_trump_month_data_sum))
            
            
         print result   
         month,rawpoll_clinton_month_data_sum,rawpoll_trump_month_data_sum,adjpoll_clinton_month_data_sum,adjpoll_trump_month_data_sum = zip(*result)
         
         print month
         print rawpoll_clinton_month_data_sum
         print rawpoll_trump_month_data_sum
         print adjpoll_clinton_month_data_sum
         print adjpoll_trump_month_data_sum
         
         fig, subplot_arr = plt.subplots(2,2, figsize=(15,10))
         x = np.arange(len(month))
         print("x",x)
         #绘制曲线图
         width =0.25
         subplot_arr[0][0].plot(rawpoll_clinton_month_data_sum,color='r')
         subplot_arr[0][0].plot(rawpoll_trump_month_data_sum,color='g')
         subplot_arr[0,0].set_xticks(x+width)
         subplot_arr[0,0].set_xticklabels(month,rotation='vertical')
#          subplot_arr[0][0].hist(rawpoll_clinton_month_data_sum,bins=10,color='b',alpha=0.3)
         
         subplot_arr[0][1].bar(x,rawpoll_clinton_month_data_sum,width,color='r')
         subplot_arr[0][1].bar(x+width,rawpoll_trump_month_data_sum,width,color='g') 
         subplot_arr[0,1].set_xticks(x+width)
         subplot_arr[0,1].set_xticklabels(month,rotation='vertical')
         
         
         
         plt.subplots_adjust(wspace=0.2)
         plt.show()
     
     
    
if __name__ == '__main__':
    run_main()