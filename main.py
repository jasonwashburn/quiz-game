from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

# loop through question data and build a bank of questions
for question in question_data:
    question_text = question['question']
    question_answer = question['correct_answer']
    question = Question(question_text, question_answer)
    question_bank.append(question)

# create our quiz
quiz = QuizBrain(question_bank)

# loop through the available questions and quiz the user
while quiz.still_has_questions():
    quiz.next_question()

# print out final results
print("You've completed the quiz.")
print(f"Your final score was {quiz.score}/{len(quiz.question_list)}")
