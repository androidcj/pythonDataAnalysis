#coding:utf-8
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import pandas as pd


def inspect_dataset(df_data):
    '''
            查看加载的数据
    '''
    print '数据信息'    
    
    print(df_data.info())
    
    print '数据集有%i行.%i列' %(df_data.shape[0],df_data.shape[1])
    print(df_data.head())



def process_missing_data(df_data):
    if df_data.isnull().values.any():
        #存在缺失数据
        df_data = df_data.fillna(0.)   #填充nan
    return df_data
        
def visualize_league_attribute(df_data,save_fig = True):
    #数据可视化
    fig = plt.figure(figsize=(15.0,10.0))
    ax1 =  fig.add_subplot(2,2,1)             
    ax2 =  fig.add_subplot(2,2,2)    
    ax3 =  fig.add_subplot(2,2,3)    
    ax4 =  fig.add_subplot(2,2,4)       
    
    plt.rcParams['font.sans-serif'] = ['SimHei']    #制定默认字体
    plt.rcParams['axes.unicode_minus'] = False #解决保存图像是负号'-'显示为方块的问题
    fig.suptitle(u'玩家属性')
    ax1.scatter(df_data['LeagueIndex'],df_data['HoursPerWeek'])
    ax1.set_xlabel(u'段位')
    ax1.set_ylabel(u'每周游戏时间')
    
    
    
    ax2.scatter(df_data['LeagueIndex'],df_data['Age'])
    ax2.set_xlabel(u'段位')
    ax2.set_ylabel(u'年龄')
    
    
    ax3.scatter(df_data['LeagueIndex'],df_data['APM'])
    ax3.set_xlabel(u'段位')
    ax3.set_ylabel(u'APM')
    
    
      
    ax4.scatter(df_data['LeagueIndex'],df_data['WorkersMade'])
    ax4.set_xlabel(u'段位')
    ax4.set_ylabel(u'单位时间建造数')
    
    if save_fig:
        plt.savefig('./league_attributes.png')
    plt.show()
    
    
def visualize_league_attribute_stats(df_data, attr_label, 
                                     savedata_path = '',
                                     savefig_path = ''):    
    """
                可视化战队属性统计值 
    """
    
    league_idx_lst = range(1,9)
    stats_min = []
    stats_max = []
    stats_mean = []
    
    for league_idx in league_idx_lst:
        filtered_data = df_data.loc[df_data['LeagueIndex']==league_idx,attr_label]    #得到该索引下  的属性值
        stats_min.append(filtered_data.min())
        stats_max.append(filtered_data.max())
        stats_mean.append(filtered_data.mean())
    
    league_ser = pd.Series(league_idx_lst,name='LeagueIndex')
    stats_min_ser = pd.Series(stats_min,name='min')
    stats_max_ser = pd.Series(stats_max,name='max')
    stats_mean_ser = pd.Series(stats_mean,name='mean')
    
    df_result = pd.concat([league_ser,stats_min_ser,stats_max_ser,stats_mean_ser],axis=1)
    
    if savedata_path !='' :
        df_result.to_csv(savedata_path,index=None)
        
        
    #图像统计
    fig = plt.figure(figsize=(15.0,10.0))
    ax1 = fig.add_subplot(1,1,1)
     # 解决matplotlib显示中文问题
    plt.rcParams['font.sans-serif'] = ['SimHei'] #指定默认字体  
    plt.rcParams['axes.unicode_minus'] = False #解决保存图像是负号'-'显示为方块的问题
    
    plt.plot(df_result['LeagueIndex'],df_result['mean'],color='b')
    plt.plot(df_result['LeagueIndex'],df_result['min'],color='g')
    plt.plot(df_result['LeagueIndex'],df_result['max'],color='r')
    
    plt.xlabel(u"阶段")
    plt.ylabel(attr_label)
    plt.title(attr_label + " vs League")
    
    
    #添加图例
    
    blue_patch = mpatches.Patch(color='blue',label='Average'+attr_label)
    green_patch = mpatches.Patch(color='green',label='Min'+attr_label)
    red_patch = mpatches.Patch(color='red',label='Max'+attr_label)
    
    plt.legend(handles=[blue_patch,green_patch,red_patch],loc=2)
    
    if savefig_path !='':
        plt.savefig(savefig_path)
    
    plt.show()       