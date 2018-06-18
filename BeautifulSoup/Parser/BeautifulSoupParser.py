import urllib2
import numpy as np
from bs4 import BeautifulSoup
def parserUrl(url):
    try:
     html= urllib2.urlopen(url)
    except Exception as e:
        print e
        return None
    try:
        nav = BeautifulSoup(html.read(),'html.parser',from_encoding='utf-8')
        spannode=nav.find("span",{"class":"nav-a-content"}).get_text()
        return spannode
    except Exception as e:    
        print e
        return None


def parserUrl_lst(url):
    try:
     html= urllib2.urlopen(url)
    except Exception as e:
        print e
        return None
    try:
        nav = BeautifulSoup(html.read(),'html.parser',from_encoding='utf-8')
        navlst = nav.find_all("span",{"class":"nav-a-content"})
        
        nvlist =[nav.get_text() for nav in navlst] 
        for nv in navlst:
            print nv.get_text()
    
        with open('./output.txt','w') as f:
            for nav_name in nvlist:
                f.write("%s\n" %nav_name.encode("utf-8"))
        return "ok"    
#         spannode=nav.find("span",{"class":"nav-a-content"}).get_text()
#         return spannode
    except Exception as e:    
        print e
        return None

def child_method(url):
    try:
     html= urllib2.urlopen(url)
    except Exception as e:
        print e
        return None
    try:
        env =  BeautifulSoup(html.read(),'html.parser',from_encoding='utf-8')
        for child in  env.find("table",{"id":"giftList"}).children:
            print child
        return "is ok"    
    except Exception as e:
        print None    
      
        
        
# html = urllib2.urlopen("https://www.amazon.cn/gp/bestsellers/books/ref=br_bsl_smr/456-4063020-4086765?pf_rd_m=A1AJ19PSB66TGU&pf_rd_s=desktop-bestsellers-2&pf_rd_r=34EJ9KWD8JZF00TKW2V3&pf_rd_r=34EJ9KWD8JZF00TKW2V3&pf_rd_t=36701&pf_rd_p=777b26ab-395a-4110-95ea-35430219c976&pf_rd_p=777b26ab-395a-4110-95ea-35430219c976&pf_rd_i=desktop")
# 
# print html.read()
# bs_obj = BeautifulSoup(html.read(),'html.parser',from_encoding='utf-8')
# nav = bs_obj.find("span" ,{"class":"nav-a-content"})
# print nav.get_text()

# url = "https://www.amazon.cn/gp/bestsellers/books/ref=br_bsl_smr/456-4063020-4086765?pf_rd_m=A1AJ19PSB66TGU&pf_rd_s=desktop-bestsellers-2&pf_rd_r=34EJ9KWD8JZF00TKW2V3&pf_rd_r=34EJ9KWD8JZF00TKW2V3&pf_rd_t=36701&pf_rd_p=777b26ab-395a-4110-95ea-35430219c976&pf_rd_p=777b26ab-395a-4110-95ea-35430219c976&pf_rd_i=desktop"

#res = parserUrl(url)
#res = parserUrl_lst(url)

url ="http://www.pythonscraping.com/pages/page3.html"

res=child_method(url)
if res==None:
    print "fail"
else:
    print res
