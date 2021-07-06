#hello.py에서 DB에 정보입력
from pymongo import MongoClient
client = MongoClient('localhost', 27017)#내 컴퓨터 mongoDB접속
db = client.dbsparta#dbsparta라는 db이름으로 접속

#1 매트릭스 별점 print
#movie = db.movies.find_one({'title': '매트릭스'})
#print(movie['star'])

#2 매트릭스와 같은 평점영화
#target_movie=db.movies.find_one({'title': '매트릭스'})
#target_star=target_movie['star']
#movies=list(db.movies.find({'star':target_star}))
#for movie in movies:
    #print(movie['title'])

#3 매트릭스 영화 평점0으로 만들기
#from pymongo import MongoClient
#client = MongoClient('localhost', 27017)
#db = client.dbsparta

#db.movies.update_one({'title':'매트릭스'},{'$set':{'star':'0'}})
