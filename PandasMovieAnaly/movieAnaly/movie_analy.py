#coding:utf-8
import pandas as pd
import matplotlib.pyplot as plt
from pandas_tool import inspect_dataset,process_missing_data,analyze_gross

dataset_path='../data/movie_metadata.csv'



def run_main():
    df_data = pd.read_csv(dataset_path)
    ## 查看数据
 #   inspect_dataset(df_data)
    
    ##处理缺失数据
    df_data = process_missing_data(df_data)
    
    #分析票房和其他因素的影响
    
    #导演和票房的关系
  #  analyze_gross(df_data,['director_name'],'../output/director_gross.csv')
    
    
    #主演与票房的关系
   # analyze_gross(df_data,['actor_1_name'],'../output/actor_gross.csv')
    
    #导演+演员 对票房的影响
   # analyze_gross(df_data,['director_name','actor_1_name'],'../output/director_actor_gross.csv')
    
    
    #查看各imdb评分的电影个数
  #  df_rating = df_data.groupby('imdb_score')['movie_title'].count()
  #  plt.figure()
  #  df_rating.plot()
  #  plt.savefig('../output/imdb_score.png')
  #  plt.show()
    
    
    #查看imdb评分最高的20部电影
   # df_directors_mean_ratings = df_data.groupby('director_name')['imdb_score'].mean()
  #  top20_imdb_directors = df_directors_mean_ratings.sort_values(ascending=False)[:20]
  #  plt.figure(figsize=(18.0,10.0))
  #  top20_imdb_directors.plot(kind='barh')
  #  plt.savefig('../output/top20_imdb_directors.png')
  #  plt.show()
  
  #电影个数分析
  #  df_genres = get_genres_data(df_data)
  #  genres_count = df_genres.groupby('genre').size()
  #  plt.figure(figsize=(15.0,10.0))
  #  genres_count.plot(kind='barh')
  #  plt.savefig('../output/genres_count.png')
  
    
    
    
    
    
    
if __name__ == '__main__':
    run_main()
    


