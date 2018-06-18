#coding:utf-8
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from bokeh.io import output_file, show
from bokeh.charts import Bar, TimeSeries
from bokeh.layouts import column
from math import pi
from IPython.core.pylabtools import figsize
from astropy.modeling import rotations


def inspact_data(air_data):
#     print '鍏辨湁%i琛岋紝%i鍒� %(air_data.shape[0],air_data.shape[1])
    print '鏁版嵁棰勮'
    print air_data.head()


def add_year_to_data(air_data):
#     date_year = air_data['Date']
    air_data['Date'] = pd.to_datetime(air_data['Date'])
    air_data['Year'] = air_data['Date'].map(lambda x:x.year)
    return air_data

def process_missing_data(df_data):
    """
                澶勭悊缂哄け鏁版嵁
    """
    
    if df_data.isnull().values.any():
        
        df_data = df_data.fillna(0.)    # 濉厖nan
#         print '瀛樺湪缂哄け鏁版嵁锛�
        
    return df_data.reset_index()
        
def plot_crashes_vs_year(air_data, method, save_fig=True):
      """
                        姣忓勾绌洪毦鏁板垎鏋�
      """
      if method == 'sns':
          
          # Seaborn 缁樺浘
         plt.figure(figsize=(15.0,10.0))
         sns.countplot(x='Year',data=air_data)
         # 瑙ｅ喅matplotlib鏄剧ず涓枃闂
         plt.rcParams['font.sans-serif'] = ['SimHei']  # 鎸囧畾榛樿瀛椾綋
         plt.rcParams['axes.unicode_minus'] = False  # 瑙ｅ喅淇濆瓨鍥惧儚鏄礋鍙�-'鏄剧ず涓烘柟鍧楃殑闂
         plt.title(u'绌洪毦娆℃暟  vs 骞翠唤')
         
         plt.xlabel(u'骞翠唤')
         plt.ylabel(u'绌洪毦娆℃暟')
         plt.xticks(rotation=90)
         
         if save_fig:
            plt.savefig('crashes_year.png')
         plt.show()
         
      elif method == 'bokeh':
             # Boken 缁樺浘
           p = Bar(air_data, 'Year', title='绌洪毦娆℃暟 vs 骞翠唤',
           plot_width=1000, 
           legend=False,
           xlabel='骞翠唤',
           ylabel='绌洪毦娆℃暟')
           p.xaxis.major_label_orientation = pi / 2
           output_file('crashes_year.html')
           show(p)   
def plot_aboard_vs_fatalities_vs_year(air_data,method,save_fig = True):
    group_year_data = air_data.groupby("Year", as_index=False).sum()
    print group_year_data
    
    if method == 'sns':
        plt.figure(figsize=(15.0,10.0))
        sns.barplot(x="Year", y="Aboard", data=group_year_data, color='green')
        sns.barplot(x="Year", y="Fatalities",data=group_year_data,color = "red")
        # 瑙ｅ喅matplotlib鏄剧ず涓枃闂
        
        plt.rcParams['font.sans-serif'] = ['SimHei']  # 鎸囧畾榛樿瀛椾綋
        plt.rcParams['axes.unicode_minus'] = False  # 瑙ｅ喅淇濆瓨鍥惧儚鏄礋鍙�-'鏄剧ず涓烘柟鍧楃殑闂
        plt.title(u'乘客数量vs遇难数vs年份')
        plt.xlabel(u'年份')
        plt.ylabel(u'乘客数量vs遇难数')
        plt.xticks(rotation =90)
        if save_fig:
            plt.savefig('aboard_fatalities_year.png')
        plt.show()
    elif method == 'bokeh':
         tsline = TimeSeries(data=group_year_data,
                            x='Year', y=['Aboard', 'Fatalities'],
                            color=['Aboard', 'Fatalities'], dash=['Aboard', 'Fatalities'],
                            title='乘客数vs遇难数vs年份', xlabel='年份', ylabel='乘客数vs遇难数',
                            legend=True)
         tspoint = TimeSeries(data=group_year_data,
                             x='Year', y=['Aboard', 'Fatalities'],
                             color=['Aboard', 'Fatalities'], dash=['Aboard', 'Fatalities'],
                             builder_type='point',
                             title='乘客数vs遇难数vs年份', xlabel='年份', ylabel='乘客数vs遇难数',
                             legend=True) 
         output_file('aboard_fatalities_year.html')
         show(column(tsline, tspoint))