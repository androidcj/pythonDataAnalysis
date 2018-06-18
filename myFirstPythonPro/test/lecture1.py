
#coding:utf-8
import numpy as np
import datetime
import matplotlib.pyplot as plt


def is_convert_float(s):
    """
        判断一个字符串能否转化为float
    """
    try:
       float(s)
    except:
       return False
    return True

def get_sum(str_array):
    cleaned_data = filter(is_convert_float, str_array)
    float_array= np.array(cleaned_data,np.float)
    return np.sum(float_array)


def run_main():
    filename = 'E:/python/lecture02_codes/codes/presidential_polls.csv'
    
    with open(filename,'r') as f:
     col_names_str = f.readline()[:-1]   #[:-1]表示不读取末尾的换行符
     col_names_lst = col_names_str.split(',')
    # print(col_names_lst)
     
    
    #使用的列明
    use_col_name_lst = ['enddate','rawpoll_clinton','rawpoll_trump','adjpoll_clinton','adjpoll_trump']
    #获取相应列名的索引
    use_col_index_lst =[col_names_lst.index(use_col_name) for use_col_name in use_col_name_lst]
    
    print ("aaa===",use_col_index_lst)
    data_array = np.loadtxt(
        filename,    #文件名
        delimiter=',',   #逗号分隔
        skiprows=1,    #跳过第一行
        dtype=str,    #string类型
        usecols=use_col_index_lst   #筛选列
        )
    
    enddate_idx = use_col_name_lst.index('enddate')
  #  print(enddate_idx)
    enddate_lst = data_array[:,enddate_idx].tolist()   #得到enddate列的所有值
 #   print(enddate_lst)
    
    #将日期格式统一  'yy-MM-dd'
    enddata_lst = [enddate.replace('-','/') for enddate in enddate_lst]
    #print(enddata_lst)
    
    #将日期字符串转化成日期
    data_lit = [datetime.datetime.strptime(enddate,'%m/%d/%Y') for enddate in enddata_lst]
    #print(data_lit[0:10])
    # 构造年份-月份列表
    month_lst= ['%d-%02d' %(date_obj.year,date_obj.month) for date_obj in data_lit]
    #得到年月数据
    month_array =np.array(month_lst) 
    
    #得到月份
    months = np.unique(month_array)
    #print(months)
    
    #统计希拉里民意投票数
    #原始数据rowpoll
    rowpoll_clinton_idx = use_col_name_lst.index('rawpoll_clinton')
    #得到希拉里民意调查数据列
    rowpoll_clinton_data = data_array[:,rowpoll_clinton_idx]
    #print(rowpoll_clinton_data)
    #得到希拉里调整后的数据
    adjpoll_clinton_idx = use_col_name_lst.index('adjpoll_clinton')
    adjpoll_clinton_data = data_array[:,adjpoll_clinton_idx]
    
    #得到trump的民意调查
    rowpoll_trump_idx = use_col_name_lst.index('rawpoll_trump')
     #得到trump民意调查数据列
    rowpoll_trump_data = data_array[:,rowpoll_trump_idx]
    
    
    #得到调整后trump的民意调查
    adjpoll_trump_idx = use_col_name_lst.index('adjpoll_trump')
       #得到trump调整后民意调查数据列
    adjpoll_trump_data = data_array[:,adjpoll_trump_idx]
    
   # print(adjpoll_clinton_data[:10])
    #保存结果
    result=[]
    for month in months:
        #希拉里  原始数据 rowpoll
        rowpoll_clinton_month_data = rowpoll_clinton_data[month_array==month]
        #统计当月总票数
        rowpoll_clinton_month_sum = get_sum(rowpoll_clinton_month_data)
        
          #希拉里  加权后的数据 adjpoll
        adjpoll_clinton_month_data = adjpoll_clinton_data[month_array==month]
        adjpoll_clinton_month_sum =  get_sum(adjpoll_clinton_month_data)
        #得到trump的票数
        rowpoll_trump_month_data = rowpoll_trump_data[month_array==month]
        rowpoll_trump_month_sum = get_sum(rowpoll_trump_month_data)
        
        adjpoll_trump_month_data = adjpoll_trump_data[month_array==month]
        adjpoll_trump_month_sum = get_sum(adjpoll_trump_month_data)
        result.append((month, rowpoll_clinton_month_sum, adjpoll_clinton_month_sum, rowpoll_trump_month_sum, adjpoll_trump_month_sum))
    print(result)
    print(rowpoll_clinton_month_sum)
    months,row_clinton_sum,adj_clinton_sum, row_trump_sum,adj_trump_sum=zip(*result)
    #可视化分析结果
    print(months)
    fig, subplot_arr = plt.subplots(2,2, figsize=(15,10))
    
    #原始数据趋势展现
    subplot_arr[0,0].plot(row_clinton_sum,color='r')
    subplot_arr[0,0].plot(row_trump_sum,color='g')
    
    width =0.25
    x = np.arange(len(months))
    subplot_arr[0,1].bar(x,row_clinton_sum,width,color='r')
    subplot_arr[0,1].bar(x+width,row_trump_sum,width,color='g')
    subplot_arr[0,1].set_xticks(x+width)
    subplot_arr[0,1].set_xticklabels(months,rotation='vertical')
    
    #调整数据趋势展现
    subplot_arr[1,0].plot(adj_clinton_sum,color='r')
    subplot_arr[1,0].plot(adj_trump_sum,color='g')
    width =0.25
    x=np.arange(len(months))
    subplot_arr[1,1].bar(x,adj_clinton_sum,width,color='r')
    subplot_arr[1,1].bar(x+ width,adj_trump_sum,width,color='g')
    subplot_arr[1,1].set_xticks(x+width)
    subplot_arr[1,1].set_xticklabels(months,rotation='vertical')
    
    plt.subplots_adjust(wspace=0.2)
    plt.show()
    
    
if __name__ == '__main__':
    run_main()