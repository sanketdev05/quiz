from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    q_text = question["text"]
    q_ans = question["answer"]
    new_question = Question(text=q_text, answer=q_ans)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()

print("You have completed the Quiz")
print(f"Your final score is {quiz.score}/{quiz.question_number}")
