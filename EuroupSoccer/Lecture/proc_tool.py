#coding:utf-8
import datetime
import numpy as np
import time

def get_age_for_football_players(birth_str):
    time.localtime(time.time())
    nowtime = time.strftime('%Y-%m-%d',time.localtime(time.time()))
    date = birth_str.split(" ")[0]
   # today = datetime.datetime.strptime("2016-12-10","%Y-%m-%d").date()
    today = datetime.datetime.strptime(nowtime,"%Y-%m-%d").date()
    born = datetime.datetime.strptime(date,"%Y-%m-%d").date()
    return today.year-born.year -((today.month,today.day) < (born.month,born.day))

def get_overall_rating(cur,player_api_id):
    """
     获得球员平均分
    """
    all_rating  =  cur.execute("SELECT overall_rating from Player_Attributes WHERE player_api_id = '%d' " %player_api_id).fetchall()
    #因为要用到numpy的操作所以转化成数组
    all_rating = np.array(all_rating,dtype=np.float)[:,0]
    #通过numpy算出平均得分
    mean_rating =  np.nanmean(all_rating)
    return mean_rating


def get_current_team_and_country(cur,player_api_id):
    """
                获取当前球队及国家
    """
    all_rating = cur.execute("SELECT overall_rating FROM Player_Attributes WHERE player_api_id = %d" %player_api_id).fetchall()
    all_rating = np.array(all_rating,dtype = np.float)[:,0]
    rating = np.nanmean(all_rating)
    
    #过滤掉有问题的评分数据
    if(rating>1):
        all_football_nums = reversed(range(1,12))    #  最多在11支球队哦待过  最少有一只球队
        for num in all_football_nums:
            all_team_id = cur.execute("SELECT home_team_api_id,country_id from Match WHERE home_player_%d = '%d'" %(num,player_api_id)).fetchall()
#             print 'bbb'
#             print  all_team_id
#             print  len(all_team_id)
        if len(all_team_id) >0:
            number_unique_teams = len(np.unique(np.array(all_team_id)[:,0]))
            last_team_id = all_team_id[-1]['home_team_api_id']
            last_country_id = all_team_id[-1]['country_id']
            last_country = cur.execute("SELECT name FROM Country WHERE id = '%d'" % (last_country_id)).fetchall()[0][0]
            last_team = cur.execute("SELECT team_long_name FROM Team WHERE team_api_id = '%d'" % (last_team_id)).fetchall()[0][0]
            print 'aaaaaaa'
            return last_team,last_country,number_unique_teams
                
    
    return None,None,0

    
    
    
