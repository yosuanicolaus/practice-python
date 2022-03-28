""" MULTIPLICATION QUIZ! """

import pyinputplus as pyip
import random
import time

tot_question = 10
correct_ans = 0

pyip.inputStr('Press Enter to begin :D', blank=True)

for question_num in range(tot_question):
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    correct = num1 * num2

    question = f'Q{question_num+1}: {num1} * {num2} = '

    try:
        pyip.inputInt(question, allowRegexes=['^%s$' % correct],
                      blockRegexes=[('.*', 'Incorrect!')],
                      timeout=8, limit=3)
    except pyip.TimeoutException:
        print('Time out!')
    except pyip.RetryLimitException:
        print('Out of tries!')
    else:
        print('Correct!')
        correct_ans += 1

time.sleep(1)
score = correct_ans / tot_question * 100
print(f'Score: {score}%')
