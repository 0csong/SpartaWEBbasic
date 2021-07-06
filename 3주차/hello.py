import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient
client = MongoClient('localhost', 27017)#내 컴퓨터 mongoDB접속
db = client.dbsparta#dbsparta라는 db이름으로 접속

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
#브라우저에서 엔터를 친것처럼
data = requests.get('https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=pnt&date=20200303',headers=headers)
#데이터 받아옴
soup = BeautifulSoup(data.text, 'html.parser')
trs=soup.select('#old_content > table > tbody > tr')
for tr in trs:
    a_tag=tr.select_one('td.title > div > a')
    if a_tag is not None:
        rank=tr.select_one('td:nth-child(1) > img')['alt']
        star=tr.select_one('td.point').text
        title=a_tag.next
        doc={
            'title':title,
            'rank':rank,
            'star':star
        }
        db.movies.insert_one(doc)
