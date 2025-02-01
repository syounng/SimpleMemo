from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient
# client = MongoClient('mongodb://soyoung:0000@172.31.44.128', 27017)
client = MongoClient('localhost', 27017)

db = client.dbjungle

## HTML을 주는 부분
@app.route('/')
def home():
   return render_template('index.html')

@app.route('/', methods=['GET'])
def read_memos():
    # mongoDB에서 _id 값을 제외한 모든 데이터 조회해오기 (Read)
    result = list(db.memos.find({}, {'_id':False}))
    # memos라는 키 값으로 memo 정보 보내주기
    return jsonify({'result': 'success', 'memos': result})


@app.route('/', methods=['POST'])
def post_memo():
    # 클라이언트로부터 데이터를 받기
    title_receive = request.form['title_give']  
    content_receive = request.form['content_give']  

    # mongoDB에 데이터를 넣기
    memo = {'title':title_receive, 'content':content_receive}
    db.memos.insert_one(memo)

    return jsonify({'result': 'success', 'msg':'POST 연결되었습니다!'})

if __name__ == '__main__':
   app.run('0.0.0.0',port=5001,debug=True)