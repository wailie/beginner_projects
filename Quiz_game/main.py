from data import question_data
from question_model import QuestionModel
from quiz_brain import QuizBrain

#question object list
questions_bank = []
for question in question_data:
    question = QuestionModel(question["text"], question["answer"])
    questions_bank.append(question)

quiz = QuizBrain(questions_bank)
while len(questions_bank) != quiz.question_number:
    quiz.next_question()
print(f"Your final score is {quiz.score}/{len(questions_bank)}")