#coding:utf-8
import pandas as pd
import matplotlib.pyplot as plt
from StarTestTools import fillNAN
def mainTask():
    data_path = 'E:/python/lecture05_codes/codes/lecture05_proj/dataset/starcraft.csv'
    data_frame= pd.read_csv(data_path)
    #得到非空数据
    df_without=fillNAN(data_frame)
    columns_name = [
                    'LeagueIndex',    #玩家索引号
                    'HoursPerWeek',   #每周游戏时间 
                    'Age',              #年龄
                    'APM',           #手速
                    'WorkersMade'    #单位建造数
                    ]
    
    df_without1 = df_without.loc[:,columns_name]
   # print(df_without1)
    #画图
    fig = plt.figure(figsize=(15.0,10.0))
    ax1 = fig.add_subplot(1,1,1);
    
    fuc = lambda f:f.max()
    print df_without1.apply(fuc)
    
    
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] =False
    ax1.scatter(df_without1['LeagueIndex'],df_without1['HoursPerWeek'])
    ax1.set_xlabel(u'段位')
    ax1.set_ylabel(u'每周游戏时间')
    plt.show()
    
  
    





if __name__=='__main__':
    mainTask()