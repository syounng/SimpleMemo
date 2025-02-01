from pymongo import MongoClient           # pymongo 라이브러리 임포트 (패키지 인스톨 먼저 해야겠죠?)
client = MongoClient('localhost', 27017)  # mongodb 서버에 연결. mongoDB는 27017가 기본 포트. localhostsms 로컬 컴퓨터에서 실행 중인 mongodb서버를 의미
db = client.jungle                        # 'jungle'라는 이름의 데이터베이스를 선택 (없으면 자동 생성)

# MongoDB에 insert 하기

# 'users'라는 collection(테이블과 비슷한 개념)에 {'name':'bobby','age':21}를 넣습니다.
# insert_one({})은 하나의 document(row와 비슷한 개념)를 삽입하는 것
db.users.insert_one({'name':'bobby','age':21}) 
db.users.insert_one({'name':'kay','age':27})
db.users.insert_one({'name':'john','age':30})

# 결과값 보기

# 여러 개 찾기
all_users = list(db.users.find({}))
same_ages = list(db.users.find({'age':21}))

print('0번째 값:')
print(all_users[0])
print('0번째 값의 이름:')
print(all_users[0]['name'])
print('모든 값:')
for user in all_users:
    print(user)

# 한 개 찾기
user1 = db.users.find_one({'name':'bobby'})
user2 = db.users.find_one({'name':'bobby'}, {'_id':False})

print('이름이 bobby인 값:')
print(user1)
print('이름이 bobby인 값의 _id를 제거한 값:')
print(user2)

# 값 수정
db.users.update_one({'name':'bobby'},{'$set':{'age':19}})
user3 = db.users.find_one({'name':'bobby'})

print('수정 결과:')
print(user3)

# 삭제
# db.users.delete_one({'name':'bobby'})
# user = db.users.find_one({'name':'bobby'})
# print(user)