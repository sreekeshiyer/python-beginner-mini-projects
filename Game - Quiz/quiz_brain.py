import random


class QuizBrain:
    def __init__(self, questions_list):
        self.question_number = 0
        self.questions_list = questions_list
        self.score = 0

    def still_has_questions(self):
        return self.question_number < len(self.questions_list)

    def next_question(self):
        self.check_answer(self.questions_list[self.question_number].answer, input(
            f"Q.{self.question_number+1} {self.questions_list[self.question_number].text} (T / F) ?"))
        self.question_number += 1

    def check_answer(self, correct_answer, user_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("That's wrong.")
        print(f"The correct answer was: {correct_answer}.")
        print(f"Your current score is: {self.score}/{self.question_number+1}")
        print("\n")
