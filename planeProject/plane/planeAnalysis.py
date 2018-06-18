#coding:utf-8
import pandas as pd
from airPlaneUtil import inspact_data,add_year_to_data,plot_crashes_vs_year,plot_aboard_vs_fatalities_vs_year

def run_main():
    filepath='Airplane_Crashes_and_Fatalities_Since_1908.csv'
    air_data=pd.read_csv(filepath)
#     inspact_data(air_data)
    
    #数据转换
    air_data = add_year_to_data(air_data)
    
    # Step.3 数据分析及可视化
    # Step. 3.1 空难数vs年份分析
 #   plot_crashes_vs_year(air_data, 'sns')
    plot_crashes_vs_year(air_data, 'bokeh')
    
#     plot_aboard_vs_fatalities_vs_year(air_data,'bokeh');
    
    return ''
    


if __name__=='__main__':
    run_main()
