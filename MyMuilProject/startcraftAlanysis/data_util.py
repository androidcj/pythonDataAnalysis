# -*- coding: utf-8 -*- 
'''

@author: caojun
'''

def clean_up_nulldata(data_f):
    if data_f.isnull().values.any():
        data_f.fillna(0.)
    return data_f
    


def featueSelect(data_f,fetures_):
    
    #得到特征筛选后的值
    furture_new_data = data_f[fetures_]
    return furture_new_data
    
    

def top_index_Apm(data_f):
    return data_f.groupby(['LeagueIndex'])['APM'].max()
    
    
    
    