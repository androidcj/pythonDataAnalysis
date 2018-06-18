#coding:utf-8
import pandas as pd
import os

def inspect_dataset(df_data):
    print '数据集基本信息'
    print df_data.info()
    print '数据集有%i行.%i列' %(df_data.shape[0],df_data.shape[1])
    print '数据预览：'
    print df_data.head()
    
#处理缺失数据
def process_missing_data(df_data):    
    if df_data.isnull().values.any():
        df_data = df_data.dropna()
    return df_data.reset_index()  

#分析票房数据并保存结果
#通过不同的列
def analyze_gross(df_data,groupby_columns,csvfile_path): 
    grouped_data = df_data.groupby(groupby_columns,as_index=False)['gross'].sum()
    #排序
    sorted_grouped_data = grouped_data.sort_values(by='gross',ascending=False)
    sorted_grouped_data.to_csv(csvfile_path)
    
def get_genres_data(df_data):
    genre_data_path = '../output/genre_data.csv'
    if os.path.exists(genre_data_path):
        print '读取电影类型数据'
        df_genre = pd.read_csv(genre_data_path)
    else:
        print '生成电影类型数据'    
        df_genre = pd.DataFrame(columns=['genre','budget','gross','year'])
        
        for i,row_data in df_data.iterrows():
            if (i+1)%100 ==0 :
                print '共%i条记录,已处理%i' %(df_data.shape[0],i+1)
            df_genre_df = convert_row_to_df(row_data)     
            df_genre = df_genre.append(df_genre_df,ignore_index=True)
            
        df_genre.to_csv('../output/genre_data.csv',index=None)    
    return df_genre


def convert_row_to_df(row_data):
    genres = row_data['genres'].split('|')
    n_genres = len(genres)
    
    dict_obj = {}
    dict_obj['budget'] = [row_data['budget']] * n_genres
    dict_obj['gross'] = [row_data['gross']] * n_genres
    dict_obj['year'] = [row_data['title_year']] * n_genres
    dict_obj['genres'] = genres
    return pd.DataFrame(dict_obj)
    
    