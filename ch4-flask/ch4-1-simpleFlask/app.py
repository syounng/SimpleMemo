# flask 서버를 돌리는 파일
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
   # flask프레임워크에 이미 구현된 내장 함수를 이용해 html을 app.py에 불러온다.
   return render_template('index.html')

@app.route('/mypage')
def mypage():  
   return 'This is My Page!'

if __name__ == '__main__':  
   app.run('0.0.0.0', port=5001, debug=True)