from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

new_q = Question("text","answer")

question_bank = []
for i in range(0,len(question_data)):
    new_q = Question(question_data[i]["question"], question_data[i]["correct_answer"])
    question_bank.append(new_q)

"""question_bank = []
for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)
print(question_bank)"""

game = QuizBrain(question_bank)

while game.still_has_questions():
    game.next_question()
print("You've completed the quiz.")
print(f"Your final score was: {game.score}/{game.question_number}")


