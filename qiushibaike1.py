import requests
from bs4 import BeautifulSoup
import re
def getpage(page):
    url='http://www.qiushibaike.com/hot/page/'+str(page)
    response=requests.get(url)
    return response
def parse(html):
    allcontent=BeautifulSoup(html,'lxml')
    contentlist=allcontent.find_all('div',attrs={'id':re.compile('qiushi_tag_.*?')})
    with open('qiushi.txt','w') as f:
        for content in contentlist:
            text=content.find('div',attrs={'class':'content'}).get_text()#正文
            vote=content.find('span',attrs={'class':'stats-vote'}).get_text()#好笑和数量
            comment=content.find('span',attrs={'class':'stats-comments'}).get_text().replace("·","")#评论和数量
            f.write(text)
            f.write(vote)
            f.write(comment)
response=getpage(3)
parse(response.text)