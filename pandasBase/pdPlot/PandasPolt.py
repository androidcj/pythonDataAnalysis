#coding:utf-8
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt  

def run_main():

#      Series的数据  线形图
#     ser_obj = pd.Series(np.random.randn(10).cumsum())
#     print ser_obj
#     ser_obj.head()
#     ser_obj.plot()
#     plt.show()
    
#     dataframe的数据    线性图
#     df_obj = pd.DataFrame(np.random.randn(10,5),columns = ['a','b','c','d','e'])
#     df_obj.plot()
#     plt.show()

#   柱状图
#       ser_obj = pd.Series(np.random.randn(10).cumsum())
#       ser_obj.plot(kind ='bar')
#       plt.show()  

#         df_obj = pd.DataFrame(np.random.randn(10,5),columns = ['a','b','c','d','e'])
#         df_obj.plot(kind ='bar')
#         plt.show()  
        
        
    #散点矩阵
     df_obj = pd.DataFrame(np.random.randn(10,5),columns = ['a','b','c','d','e'])
     pd.scatter_matrix(df_obj)
     plt.show() 
        

if __name__=='__main__':
    run_main()


