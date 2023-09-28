from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication,QWidget,QHBoxLayout,QVBoxLayout,QGroupBox,QRadioButton,QPushButton,QLabel,QButtonGroup)
def show_result():
    RadioGroupBox.hide()
    RadioGroupBox_2.show()
    button_2.setText('Следующий вопрос')
#answer = [rbtn_1,rbtn_2,rbtn_3,rbtn_4]
app = QApplication([])
window = QWidget()
window.resize(400,240)
window.setWindowTitle('Memory Card')

class Question():
    def __init__(self,question,right_answer,wrong_1,wrong_2,wrong_3):
        self.question = question
        self.right_answer = right_answer
        self.wrong_1 = wrong_1
        self.wrong_2 = wrong_2
        self.wrong_3 = wrong_3

button_1= QLabel ('Какой национальности не существует?')
button_2 = QPushButton('Ответить')

RadioGroupBox = QGroupBox('Варианты ответов')
rbtn_1 = QRadioButton ('Энцы')
rbtn_2 = QRadioButton ('Смурфы')
rbtn_3 = QRadioButton ('Чулымцы')
rbtn_4 = QRadioButton ('Алеуты')

answer = [rbtn_1,rbtn_2,rbtn_3,rbtn_4]

RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)

def show_question():
    button_2.setText('Ответить')
    RadioGroupBox_2.hide()
    RadioGroupBox.show()
    RadioGroup.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True)

def click_ok():
    if button_2.text() == 'Ответить':
        show_result()
    elif next_question() == 'Следующий вопрос':
        next_question()


def ask(q:Question):
    shuffle(answer)
    button_1.setText(q.question)
    answer[0].setText(q.right_answer)
    answer[1].setText(q.wrong_1)
    answer[2].setText(q.wrong_2)
    answer[3].setText(q.wrong_3)
    bask.setText('Правильный ответ')
    show_question()

question_list = []
question_list.append(Question('Государсвенный язык Португалии','Португальский','Английский','Испанский','Французский'))
question_list.append(Question('Река,протекающая в бразильских тропических лесах','Амазонка','Нил','Волга','Конго'))
question_list.append(Question('Столица Канады','Оттава','Лиссабон','Мадрид','Прага'))
RadioGroupBox_2 = QGroupBox('Результат теста')
RadioGroupBox_2.hide()

def check_answer():
    if answer[0].isChecked():
        show_correct('Правильно')
    else:
        if answer[1].isChecked() or answer[2].isChecked() or answer[3].isChecked():
            show_correct('Неправильно')

def show_correct(ans):
    rask.setText(ans)
    show_result()

window.cur_question = -1   

def next_question():
    window.cur_question +=1
    if window.cur_question == len(question_list):
        window.cur_question = 0
    ask(question_list[window.cur_question])

cur_question = randint(0,len(question_list) -1)
q = question_list[cur_question]


    
layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()

layout_ans2.addWidget(rbtn_1)
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3)
layout_ans3.addWidget(rbtn_4)
layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)

RadioGroupBox.setLayout(layout_ans1)

rask = QLabel ('Правильно/Неправильно')
bask = QLabel ('Правильный ответ')

layout_ans_1 = QVBoxLayout()

layout_ans_1.addWidget(rask)
layout_ans_1.addWidget(bask, alignment=Qt.AlignCenter)

RadioGroupBox_2.setLayout(layout_ans_1)

main_layout = QVBoxLayout()
main_layout.addWidget(button_1, alignment = Qt.AlignVCenter)
main_layout.addWidget(RadioGroupBox, alignment = Qt.AlignVCenter)
main_layout.addWidget(RadioGroupBox_2, alignment = Qt.AlignVCenter)

main_layout.addWidget(button_2, alignment = Qt.AlignVCenter)
ask(question_list[1])
button_2.clicked.connect(click_ok) 

window.setLayout(main_layout)

window.show()
app.exec_()





