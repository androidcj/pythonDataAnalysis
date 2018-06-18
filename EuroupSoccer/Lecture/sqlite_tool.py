#coding:utf-8
import sqlite3

def connect_sqlite(sqlite_file):
    """
    连接数据库 返回游标
    """
    with sqlite3.connect(sqlite_file) as conn:
        conn.row_factory = sqlite3.Row    #返回的每行是sqliteRow  可以通过列名返回
        cur = conn.cursor()
        return conn,cur
    
    
def close_sqlite(conn):
    """
    关闭连接
    """
    if conn: 
        conn.close()
    
        
    
     
     
