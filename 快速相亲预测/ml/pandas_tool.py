#coding:utf-8
from pandas.algos import left_join_indexer_float32

#处理缺失数据
def process_miss_data(df_data):
    #全部转化成小写
    df_data['field'] = df_data['field'].str.lower()
    if df_data[['field','field_cd']].isnull().values.any():
        #根据行业 补全行业代码的缺失值
        
        #获取行业和行业代码的唯一值数据
        df_field_and_fcd = df_data[['field','field_cd']].drop_duplicates()
        
        #删除存在nan的行
        df_field_and_fcd = df_field_and_fcd.dropna()
        
        #生成字典
        fcd_dict = dict(zip(df_field_and_fcd['field'],df_field_and_fcd['field_cd']))
        #找到缺失 行业代码的索引列
        fcd_null_index_lst = df_data[df_data['field_cd'].isnull() & ~df_data['field'].isnull()].index.tolist()
        
        #根据字段补全数据
        for fcd_null_index in fcd_null_index_lst:
            field_key = df_data.ix[fcd_null_index,'field']
            df_data.ix[fcd_null_index,'field_cd'] = fcd_dict[field_key]
        print '补全了%d条 行业代码缺失数据'  %len(fcd_null_index_lst) 
        
    return   df_data

def get_pair_data(df_data,save_filepath='./processed_dataset.csv'):
     # 使用的特征列表
    used_feat_lst = ['iid', 'gender', 'pid', 'match', 'samerace', 
                     'age_o', 'race_o', 'pf_o_att', 'pf_o_sin', 'pf_o_int','pf_o_fun', 'pf_o_amb', 'pf_o_sha',
                     'age', 'field_cd', 'race', 'imprace', 'imprelig', 'goal', 'date', 'go_out', 
                     'sports', 'tvsports', 'exercise', 'dining', 'museums', 'art', 'hiking', 'gaming', 'clubbing',
                     'reading', 'tv', 'theater', 'movies', 'concerts', 'music', 'shopping', 'yoga', 'exphappy',
                     'attr1_1', 'sinc1_1', 'intel1_1', 'fun1_1', 'amb1_1', 'shar1_1', 
                     'attr2_1', 'sinc2_1', 'intel2_1', 'fun2_1', 'amb2_1', 'shar2_1', 
                     'attr3_1', 'sinc3_1', 'intel3_1', 'fun3_1', 'amb3_1']
    
    used_df_data = df_data[used_feat_lst]
    cleaned_df_data= used_df_data.dropna()
    cleaned_df_data = cleaned_df_data.reset_index()
    
    #根据性别构建男性，女性数据
    m_df_data = cleaned_df_data[cleaned_df_data['gender']==1]
    print '得到男性数据：',m_df_data.shape
    
    #得到女性数据
    f_df_data = cleaned_df_data[cleaned_df_data['gender']==0]
    
    print '得到女性数据：',f_df_data.shape
    
    
    #男性特征列表
    m_feat_lst = ['iid', 'pid', 'match', 'samerace', 'age', 'field_cd', 'race', 
                  'imprace', 'imprelig', 'goal', 'date', 'go_out', 
                  'sports', 'tvsports', 'exercise', 'dining', 'museums', 'art', 'hiking', 'gaming', 'clubbing',
                  'reading', 'tv', 'theater', 'movies', 'concerts', 'music', 'shopping', 'yoga', 'exphappy',
                  'attr1_1', 'sinc1_1', 'intel1_1', 'fun1_1', 'amb1_1', 'shar1_1', 
                  'attr2_1', 'sinc2_1', 'intel2_1', 'fun2_1', 'amb2_1', 'shar2_1', 
                  'attr3_1', 'sinc3_1','fun3_1', 'intel3_1', 'amb3_1']
    new_m_data = m_df_data[m_feat_lst]
    
    
    #女性特征
    f_feat_lst =[m_feat_lst[0]]+m_feat_lst[4:] 
    
    #获取女性唯一数据
    new_f_data = f_df_data[f_feat_lst].drop_duplicates()
    
    #重命名女性特征列名  ，添加前缀'f'
    new_f_data.columns =[('f_'+ name) for name in f_feat_lst ]
    print '构建成对数据'
    
    
    #数据表连接
    pair_df_data = new_m_data.merge(new_f_data,how='left',left_on='pid',right_on='f_iid')
    
    #去除nan数据
    pair_df_data =pair_df_data.dropna()
    
    #去除ID列表
    drop_feat_lst = ['iid','pid','f_iid']
    pair_df_data = pair_df_data.drop(drop_feat_lst,axis=1)
    
   # print pair_df_data
    
  #  print '数据重构完成'
   #保存数据
    pair_df_data.to_csv('../temp.csv',index=None)
      #分割数据与标签
    pair_data = pair_df_data.drop('match',axis=1).values
    labels = pair_df_data['match'].values
    features = pair_df_data.drop('match',axis=1).columns
    
    return pair_data,labels,features
    
    