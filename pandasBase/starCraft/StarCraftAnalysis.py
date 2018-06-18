#coding:utf-8
import pandas as pd
from pandas_tools import inspect_dataset,visualize_league_attribute,\
visualize_league_attribute_stats,process_missing_data

def run_main():
   data_path = 'E:/python/lecture05_codes/codes/lecture05_proj/dataset/starcraft.csv'
    
   df_data = pd.read_csv(data_path)
    #查看数据
   inspect_dataset(df_data)
    
    ##处理缺失数据
   df_data = process_missing_data(df_data)
    
   columns_name = [
                    'LeagueIndex',    #玩家索引号
                    'HoursPerWeek',   #每周游戏时间 
                    'Age',              #年龄
                    'APM',           #手速
                    'WorkersMade'    #单位建造数
                    ]
   visualize_league_attribute(df_data[columns_name])
    
    
   #得到段位属性值 
   visualize_league_attribute_stats(
       df_data[columns_name],
       'APM',
       savedata_path ='./league_apm_states.csv',
       savefig_path ='./league_apm_states.png',
       )
    
   visualize_league_attribute_stats(
       df_data[columns_name],
       'HoursPerWeek',
       savedata_path ='./league_hoursweek_states.csv',
       savefig_path ='./league_hoursweek_states.png',
       )
   print 'aaa'



if __name__ == '__main__':
    run_main()