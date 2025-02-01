from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbjungle 

# ‘포레스트 검프'의 개봉 연도를 가져오기

# 방법 1
for movie in db.movies.find():
    if movie['title']=='포레스트 검프':
        print(movie['released_year'])
        break

# 방법 2
movie = db.movies.find_one({'title':'포레스트 검프'})
print(movie['released_year'])

# '포레스트 검포'와 같은 년도에 개봉한 영화 제목들을 가져오기

target_movie = db.movies.find_one({'title':'포레스트 검프'})
target_year = target_movie['released_year']

# 방법 1
for x in db.movies.find():
    if x['released_year'] == target_year:
        print(x['title'])

# 방법 2
movies = list(db.movies.find({'released_year':target_year}))
for movie in movies:
    print(movie['title'])

# '매트릭스 영화'의 개봉 연도를 1998년으로 만들기

print('수정 전:')
print(db.movies.find_one({'title':'매트릭스'})['released_year'])
db.movies.update_one({'title':'매트릭스'}, {'$set':{'released_year':1998}})
print('수정 후:')
print(db.movies.find_one({'title':'매트릭스'})['released_year'])
db.movies.update_one({'title':'매트릭스'}, {'$set':{'released_year':1999}})
