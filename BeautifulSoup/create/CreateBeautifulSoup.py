from bs4 import BeautifulSoup
import urllib2

#html = urllib2.urlopen("http://www.baidu.com/")
#bs_obj = BeautifulSoup(html,'html.parser',from_encoding ='utf-8')
#print "title_tag:",bs_obj.html


html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""


#bs_obj = BeautifulSoup(html_doc, 'html.parser', from_encoding='utf-8')

#linklist = bs_obj.find_all('a')
#linklist = bs_obj.find_all('a',id='link2')
#linklist = bs_obj.find_all('a',class_='sister')

#for link in linklist:
 #   print link.name,link['href'],link.get_text()
    
    
    
def get_html_title(url):
    
    try:
        html = urllib2.urlopen(url)
    except Exception as e:
        print e
        return None
    
    
    try:
        bs_obj = BeautifulSoup(html.read(),'html.parser',from_encoding='utf-8')
        title = bs_obj.title
    except Exception as e:
         return None
     
    return title    





title = get_html_title("http://www.taobao.com")
if title !=None:
    print title
else:
    print "title fail"   