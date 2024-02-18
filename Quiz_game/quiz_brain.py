class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0


    def next_question(self):
        current_question = self.question_list[self.question_number]
        user_answer = input(f"Q.{self.question_number + 1} {current_question.text} (True/False)? ")
        self.check_answer(user_answer, current_question.answer)
        self.question_number += 1

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print(f"You got it right!\nThe correct answer was {correct_answer}.")
        else:
            print(f"That was wrong.\nThe correct answer was {correct_answer}.")

        print(f"Your score is {self.score}/{self.question_number + 1}\n")
