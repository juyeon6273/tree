from flask import Flask, render_template, request, jsonify, redirect, url_for
import json
from keybert import KeyBERT
import random

app = Flask(__name__)  # Flask 객체 생성

model = KeyBERT()

class Game:
    def __init__(self, questions, options, answer):
        self.question_number = 0
        self.selected_option = None
        self.number_of_questions = len(questions)
        self.correct_answer_numbers = 0
        self.questions = questions
        self.options = options
        self.answer = answer

    def check_answer(self, question_number):
        if self.selected_option == answer[question_number]:
            return True

    def next_question(self):
        if self.selected_option is not None:
            if self.check_answer(self.question_number):
                self.correct_answer_numbers += 1

            self.question_number += 1

        if self.question_number == self.number_of_questions:
            return True
        else:
            return False

    def get_question_data(self):
        question_data = {}
        if self.question_number < self.number_of_questions:
            question_data['question'] = questions[self.question_number]["question"]
            question_data['options'] = options[self.question_number]
            return question_data
        return None

    def reset(self):
        self.question_number = 0
        self.selected_option = None
        self.correct_answer_numbers = 0

# informations.json 파일에서 데이터 로드
with open('informations.json', encoding='utf-8') as f:
    info = json.load(f)

questions = info['questions']
question_type = ["writing", "voca", "background", 'reading']

question = [q["question"] for q in questions]
options = [q["options"] for q in questions]
answer = [q["answer"] for q in questions]

# 게임 초기화
game = Game(questions, options, answer)

@app.route('/')
def index():
    return render_template('index.html')

# 퀴즈 페이지 설정
@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    if request.method == 'POST':
        selected_option = int(request.form['option'])
        game.selected_option = selected_option

        if game.next_question():
            return redirect(url_for('result'))

    question_data = game.get_question_data()
    return render_template('quiz.html', question_data=question_data)

# 결과 페이지 설정
@app.route('/result')
def result():
    score = (game.correct_answer_numbers / game.number_of_questions) * 100
    return render_template('result.html', score=score)

# reset 설정
@app.route('/reset', methods=['POST'])
def reset():
    game.reset()
    return redirect(url_for('quiz'))

if __name__ == '__main__':
    app.run(debug=True)