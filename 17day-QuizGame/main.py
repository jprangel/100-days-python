from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

q_bank = []

for i in question_data:
    t = i['question']
    a = i['correct_answer']
    q_obj = Question(t, a)
    q_bank.append(q_obj)

quiz = QuizBrain(q_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You have completed your quiz")
print(f"Your final score is {quiz.score}/{quiz.question_number}")
