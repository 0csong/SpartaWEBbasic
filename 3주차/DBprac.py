from pymongo import MongoClient
client = MongoClient('localhost', 27017)#내 컴퓨터 mongoDB접속
db = client.dbsparta#dbsparta라는 db이름으로 접속
#insert/find/update/delete
# 삽입 - 예시
#doc = {'name':'bobby','age':25}
#db.users.insert_one(doc)

# 한 개 찾기 - 예시
#user = db.users.find_one({'name':'bobby'})
#print(user)

# 여러개 찾기 - 예시 ( _id 값은 제외하고 출력)
#same_ages = list(db.users.find({'age':21},{'_id':False}))
#print(same_ages[0]['name'])

# 바꾸기 - 예시
#db.users.update_one({'name':'bobby'},{'$set':{'age':19}})

# 지우기 - 예시
#db.users.delete_one({'name':'bobby'})
