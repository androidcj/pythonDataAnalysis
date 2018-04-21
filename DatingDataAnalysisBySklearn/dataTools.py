# -*- coding: utf-8 -*- 
'''
Created on 2018年4月21日

@author: caojun
'''

#去除空值
def data_drop_na(data_df):
    if data_df.isnull().values.any():
        data_df.dropna();
    return data_df


def get_pair_data(data_df):   
    # 使用的特征列表
    used_feat_lst = ['iid', 'gender', 'pid', 'match', 'samerace', 
                     'age_o', 'race_o', 'pf_o_att', 'pf_o_sin', 'pf_o_int','pf_o_fun', 'pf_o_amb', 'pf_o_sha',
                     'age', 'field_cd', 'race', 'imprace', 'imprelig', 'goal', 'date', 'go_out', 
                     'sports', 'tvsports', 'exercise', 'dining', 'museums', 'art', 'hiking', 'gaming', 'clubbing',
                     'reading', 'tv', 'theater', 'movies', 'concerts', 'music', 'shopping', 'yoga', 'exphappy',
                     'attr1_1', 'sinc1_1', 'intel1_1', 'fun1_1', 'amb1_1', 'shar1_1', 
                     'attr2_1', 'sinc2_1', 'intel2_1', 'fun2_1', 'amb2_1', 'shar2_1', 
                     'attr3_1', 'sinc3_1', 'intel3_1', 'fun3_1', 'amb3_1'] 
    
    used_feat_data = data_df[used_feat_lst]
    used_feat_data = used_feat_data.dropna()
    
    m_feat_data = used_feat_data[used_feat_data['gender'] == 1]    #得到男性
    f_feat_data = used_feat_data[used_feat_data['gender'] == 0]    #得到女性
    
    # 男性特征列表
    m_feat_lst = ['iid', 'pid', 'match', 'samerace', 'age', 'field_cd', 'race', 
                  'imprace', 'imprelig', 'goal', 'date', 'go_out', 
                  'sports', 'tvsports', 'exercise', 'dining', 'museums', 'art', 'hiking', 'gaming', 'clubbing',
                  'reading', 'tv', 'theater', 'movies', 'concerts', 'music', 'shopping', 'yoga', 'exphappy',
                  'attr1_1', 'sinc1_1', 'intel1_1', 'fun1_1', 'amb1_1', 'shar1_1', 
                  'attr2_1', 'sinc2_1', 'intel2_1', 'fun2_1', 'amb2_1', 'shar2_1', 
                  'attr3_1', 'sinc3_1','fun3_1', 'intel3_1', 'amb3_1']
    
    m_feat_data = m_feat_data[m_feat_lst]
        # 女性特征列表
    f_feat_lst = [m_feat_lst[0]] + m_feat_lst[4:]
    
    f_feat_data = f_feat_data[f_feat_lst].drop_duplicates()
    
    # 重命名女性特征列名，添加前缀'f'
    f_feat_data.columns = [ ('f_' + i) for i in f_feat_lst]
    
    #得到关联之后的数据
    pair_data = m_feat_data.merge(f_feat_data,left_on = 'pid',right_on='f_iid',how='left')
    pair_data = pair_data.dropna()
    pair_data.drop(['iid', 'pid', 'f_iid'],axis = 1)
    
    print('数据组合已完成')
    
#     print(pair_data)
    
    res_data = pair_data.drop(['match'],axis=1).values
    labels = pair_data['match'].values
    feachers = pair_data.drop(['match'],axis=1).columns
    return res_data,labels,feachers
    
    
    
    