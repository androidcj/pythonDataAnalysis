# -*- coding: utf-8 -*- 

'''
电影数据分析

Created on 2018年3月18日

@author: caojun
'''
import pandas as pd
from data_util import analyze_gross
import matplotlib.pyplot as plot

def run_main():
    
    data_movie = pd.read_csv('data/movie_metadata.csv')
    #print(data_movie)
    
    #导演和票房的关系
    analyze_gross(data_movie,['director_name'],'./out/director_gross.csv')
    
    
    #主演与票房的关系
    analyze_gross(data_movie,['actor_1_name'],'./out/actor_gross.csv')
    
    
#     imbadata = data_movie.groupby('imdb_score')['movie_title'].count()
   
   # plot.figure()
  # imbadata.plot()
    #plot.show()
    
    #得到排名前20名导演
    imbadata = data_movie.groupby('director_name')['imdb_score'].mean()
    top_20_data = imbadata.sort_values(ascending=False)[:20]
    #print(top_20_data)
    plot.figure(figsize=(18.0,10.0))
    top_20_data.plot(kind='barh')
    plot.show()
    return ''
    
    



if __name__=='__main__':
    run_main()



