from question_model import Model
from data import questions
from quiz_brain import QuizBrain

questions_list = []


for question in questions:
    q_text = question["question"]
    q_answer = question["correct_answer"]
    model = Model(q_text, q_answer)
    questions_list.append(model.question)

quizbrain = QuizBrain(questions_list)

while quizbrain.still_has_question():
    quizbrain.next_question()
    

