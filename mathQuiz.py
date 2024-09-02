import pyinputplus as pyip
import random, time
#define the numbber of tries
number_of_questions = 10
correctAnswers = 0
for question_numer in range(number_of_questions):
    # picking random numbers
    num1 = random.randint(0,9)
    num2 = random.randint(0,9)
    # call the prompt function
    prompt = '#%s: %s x %s = ?\n' % (question_number, num1, num2)
    try:
        # rigtht answers are handled by allowed_regex
        # wrong answers are handled by block_regex
        