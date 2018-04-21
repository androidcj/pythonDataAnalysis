# -*- coding: utf-8 -*- 
'''

pandas工具类
@author: caojun
'''

def handle_missing_data(df_data):
    if df_data.isnull().values.any():
        df_data.dropna()
    
    df_data.reset_index()
    
    
def analyze_gross(df_data,groupby_columns,outputFile):
    
    res_data = df_data.groupby(groupby_columns,as_index=True).sum()
    sorted_grouped_data = res_data.sort_values(by='gross',ascending=False)
    sorted_grouped_data.to_csv(outputFile)
    