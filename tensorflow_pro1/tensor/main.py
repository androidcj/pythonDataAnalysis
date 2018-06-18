#coding:utf-8

'''
Created on 2018.4.29

@author: caojun
'''

import tensorflow as tf  
  
def run_main():
    sess = tf.Session()
    
#     a = tf.constant([1.0,2.0],name='a')
#     b = tf.constant([1.0,2.0],name='b')
#     result = tf.add(a, b, name='add')
#     print(result)
#     print(a.graph == tf.get_default_graph)
#     print(result.get_shape())
#     print(tf.Session().run(result))

#     a = tf.placeholder(tf.float32)
#     b = tf.placeholder(tf.float32)
#     add_node = a+b
#     
# #     result = sess.run(add_node, {a:1.0,b:4.5})
#     add_and_trip = add_node * 3
#     result = sess.run(add_and_trip, {a:1.0,b:4.5})
#     print(result)
    
    #线性回归例子
    w = tf.Variable([.3],dtype=tf.float32)
    b = tf.Variable([-.3],dtype=tf.float32)
    x = tf.placeholder(tf.float32)
    liner_model = w*x+b
    #初始化参数
    init = tf.global_variables_initializer()
    sess.run(init)
    result = sess.run(liner_model,{x:[1,2,3,4]})
    print(result)
    
    
    return ''


if __name__ == '__main__':
    run_main()