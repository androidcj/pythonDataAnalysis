# -*- coding: utf-8 -*- 

'''

@author:caojun
'''
import pandas as pd
from startcraftAlanysis.data_util import clean_up_nulldata,featueSelect,\
    top_index_Apm

import matplotlib.pyplot as plt

def run_main():
    data_path = './data/starcraft.csv'
    s_data = pd.read_csv(data_path)
#     print('orin==',s_data.shape[0])
    
    
    s_data = clean_up_nulldata1(s_data)
#     print('orin111==',s_data)
    #筛选特征
    s_feature = ['GameID','LeagueIndex','Age','TotalHours','APM']
    s_data = select_feature_nums1(s_data,s_feature)
    
#     s_data =  clean_up_nulldata(s_data)
#     print('rev==',s_data.shape[0])
    
#     s_feature = ['GameID','LeagueIndex','Age','TotalHours','APM']
#     s_data = featueSelect(s_data,s_feature)
    
  
    
    #得到每个联赛等级APM最高的gameID
#     top_apm = top_index_Apm(s_data)
#     print(top_apm)
    
    s_data = top_index_Apm(s_data)
    s_data.plot()
    plt.show()
    
    return ''

def clean_up_nulldata1(data_path):
    if data_path.isnull().values.any():
        data_path.fillna(0.);
    return data_path


def select_feature_nums1(s_data,attrs):
#     print(s_data.head())
    return s_data.loc[:,attrs];

def top_index_Apm(s_data):
    max_apms = s_data.groupby('LeagueIndex')[['APM','GameID']].max()
    return max_apms

if __name__ =='__main__':
    run_main()
    