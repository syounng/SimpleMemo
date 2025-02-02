from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient
# client = MongoClient('mongodb://soyoung:0000@172.31.44.128', 27017)
client = MongoClient('localhost', 27017)

# mongodb의 objectid 사용을 위해 임포트
from bson import ObjectId

db = client.dbjungle

## HTML을 주는 부분
@app.route('/')
def home():
   return render_template('index.html')

@app.route('/memos', methods=['GET'])
def read_memos():
    # mongoDB에서 모든 데이터 조회해오기 (Read)
    memos = list(db.memos.find({}, {'_id':True, 'title':True, 'content':True, 'likes':True}))
    result = []

    # 몽고디비에 저장된 id 값을 문자열로 변환 
    # 몽고디비에 저장된 likes 값을 정수로 변환 (정렬하기 위해)
    for memo in memos:
        memo['_id'] = str(memo['_id'])
        memo['likes'] = int(memo['likes'])
        result.append(memo)

    # likes 많은 순으로 정렬
    result.sort(key=lambda x: -x['likes'])

    # memos라는 키 값으로 memo 정보 보내주기
    return jsonify({'result': 'success', 'memos': result})


@app.route('/memos', methods=['POST'])
def post_memo():
    # 클라이언트로부터 데이터를 받기
    title_receive = request.form['title_give']  
    content_receive = request.form['content_give']  
    likes = 0

    # mongoDB에 데이터를 넣기
    memo = {'title':title_receive, 'content':content_receive, 'likes': likes}
    db.memos.insert_one(memo)

    return jsonify({'result': 'success', 'msg':'POST 연결되었습니다!'})

@app.route('/memos', methods=['DELETE'])
def delete_memo():

    # id 받아오기
    id_receive = request.form['id_give']  
    print('삭제할 아이디:', id_receive)

    # 받은 id를 objectid로 변환
    object_id = ObjectId(id_receive)

    # 몽고디비에서 삭제
    result = db.memos.delete_one({'_id':object_id})

    return jsonify({'result': 'succes', 'msg':'DELETE 성공'})

@app.route('/memos', methods=['PUT'])
def put_memo():
    
    # id 받아오기
    id_receive = request.form['id_give']  
    title_receive = request.form['title_give']  
    content_receive = request.form['content_give']  
    
    print('값 받아오기 완료')

    print('수정할 아이디:', id_receive)

    # 받은 id를 objectid로 변환
    object_id = ObjectId(id_receive)

    # 몽고디비에서 값을 없데이트
    result = db.memos.update_one(
        {'_id':object_id}, 
        {'$set': {'title': title_receive, 'content': content_receive}}
    )

    return jsonify({'result': 'success', 'msg':'수정이 완료되었습니다.'})

@app.route('/likes', methods=['PUT'])
def put_likes():
    # id 받아오기
    id_receive = request.form['id_give']
    likes_receive = request.form['likes_give']

    print('값 받아오기 완료')
    print('좋아요 수정할 아이디:', id_receive)

    # 받은 id를 objectid로 변환
    object_id = ObjectId(id_receive)
    
    # 몽고디비에서 값을 없데이트
    result = db.memos.update_one(
        {'_id': object_id}, 
        {'$set': {'likes':likes_receive}}
    )

    return jsonify({'result': 'success', 'msg':'좋아요가 반영되었습니다.'})




if __name__ == '__main__':
   app.run('0.0.0.0',port=5001,debug=True)