from flask import Flask, render_template
import json
import random
import os

app = Flask(__name__)

# directory 경로 설정
directory = "C:/Users/jyeon/PycharmProjects/Python-Quiz-Game/DatasetBlank"

# 디렉토리 내의 파일 목록을 가져옴
file_list = os.listdir(directory)

# 디렉토리 내에서 무작위로 파일 선택
random_file = random.choice(file_list)

# 파일 이름과 확장자를 분리
file_name, file_extension = os.path.splitext(random_file)

# 파일 경로 생성
file_path = os.path.join(directory, random_file)

with open('informations.json', 'r', encoding='utf-8') as json_file:
    data = json.load(json_file)

for question in data['questions']:
    question['id'] = 1
    question['question_type'] = "writing"
    question['question'] = "빈칸에 들어갈 단어(어휘)를 쓰시오"
    question['options'] = ["summary1", "false1", "false2", "false3"]
    question['answer'] = 1
    question['passage'] = file_path

with open('informations.json', 'w', encoding='utf-8') as json_file:
    json.dump(data, json_file, ensure_ascii=False, indent=4)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/quiz')
def quiz():
    # 퀴즈 페이지를 표시하기 위한 데이터 로직 추가
    return render_template('quiz.html')

@app.route('/result')
def result():
    # 결과 페이지를 표시하기 위한 데이터 로직 추가
    return render_template('result.html')

@app.route('/quiz_front')
def quiz_front():
    return render_template('quiz_front.html')  # quiz_front.html 파일을 렌더링

if __name__ == '__main__':
    app.run(debug=True)
