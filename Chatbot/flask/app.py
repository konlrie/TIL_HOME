import random
from datetime import datetime
from flask import Flask, render_template, request
app = Flask(__name__)

# @app.route('/')
# def hello_world():
#     return '바로 바뀐다!'

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/mulcam')
def mulcam():
    return '20층 스카이라운지!'

# @app.route('/dday')
# def dday():
#     today = datetime.now()
#     new_year = datetime(2020, 1, 1)
#     result = new_year - today
#     return f'<h1>더 성숙해지기까지 {result.days}일 남았습니다!</h1>'

# 인사해주는 페이지
# @app.route('/greeting/<string:name>')
# def greeting(name):
#     return f'{name}님 안녕?'

# 인사하는 페이지
@app.route('/greeting/<string:name>')
def greeting(name):
    return render_template('greeting.html', html_name=name)

# 세제곱을 돌려주는 페이지
@app.route('/cube/<int:number>')
def cube(number):
    result = number ** 3
    return render_template('cube.html', number=number, result=result)

@app.route('/movie')
def movie():
    movies = ['나이브스 아웃', '기생충', '엔드게임']
    return render_template('movie.html', movie_list=movies)

@app.route('/ping')
def ping():
    return render_template('ping.html')

@app.route('/pong')
def pong():
    age = request.args.get('age')
    return render_template('pong.html', age=age)

@app.route('/naver')
def naver():
    return render_template('naver.html')

@app.route('/google')
def google():
    return render_template('google.html')

# 사용자로부터 입력받을 페이지를 렌더링해줌.
@app.route('/vonvon')
def vonvon():
    return render_template('vonvon.html')

# 요청을 받은 뒤 데이터를 가공해서 사용자에게 응답해줌.
@app.route('/godmademe')
def godmademe():
    name = request.args.get('name')
    # 데이터 리스트
    first_options = ['잘생김', '못생김', '존잘', '존못', '쏘쏘']
    second_options = ['친절함', '싹수', '애교', '잘난척']
    third_options = ['돈복', '코딩력', '물욕', '식욕']

    # 각 데이터 리스트 별로 요소를 하나씩 무작위로 뽑음
    tmp = random.sample(first_options, 1)
    print(tmp, type(tmp), tmp[0])
    first = random.choice(first_options)
    print(first, type(first))
    second = random.choice(second_options)
    third = random.choice(third_options)

    # 뽑은 데이터를 템플릿에 넘겨줌
    return render_template('godmademe.html', name=name, first=first, second=second, third=third)

# (중요) app.py 가장 하단에 위치
if __name__ == '__main__':
    app.run(debug=True)