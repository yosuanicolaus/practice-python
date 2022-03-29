"""Project: Generating Random Quiz Files

Say you're a geography teacher with 35 students in your class and you want to give a pop quiz on US state capitals. Alas, your class has a few bad eggs in it, and you can't trust the students not to cheat. You'd like to randomize the order of questions so that each quiz is unique, making it impossible for anyone to crib answers from anyone else. Of course, doing this by hand would be a lengthy and boring affair. Fortunately, you know some Python.

Here is what the program does:

    Creates 35 different quizzes
    Creates 50 multiple-choice questions for each quiz, in random order
    Provides the correct answer and three random wrong answers for each question, in random order
    Writes the quizzes to 35 text files
    Writes the answer keys to 35 text files

This means the code will need to do the following:

    Store the states and their capitals in a dictionary
    Call open(), write(), and close() for the quiz and answer key text files
    Use random.shuffle() to randomize the order of the questions and multiple-choice options
"""

import random
import pprint

capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
            'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
            'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
            'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
            'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
            'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
            'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
            'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
            'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
            'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton',
            'New Mexico': 'Santa Fe', 'New York': 'Albany',
            'North Carolina': 'Raleigh', 'North Dakota': 'Bismarck', 'Ohio': 'Columbus',
            'Oklahoma': 'Oklahoma City',
            'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
            'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
            'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
            'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia',
            'West Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

key_ans = {}


def create_question(num: int, capital: str) -> str:
    question = f'{num}. What is the capital of {capital}?\n'
    correct_ans = capitals[capital]
    random_list = list(capitals.values())
    del random_list[random_list.index(correct_ans)]
    random_ans = random.sample(random_list, 3)
    choices = [correct_ans, *random_ans]
    random.shuffle(choices)
    for i in range(4):
        question += '   ' + 'ABCD'[i] + '. ' + choices[i] + '\n'
    question += '\n'
    key_ans[f'{num:02d}'] = ('ABCD'[choices.index(correct_ans)])
    return question


def create_quiz(quiznum: int) -> None:
    '''a quiz for 1 student, which consists of
    50 random ordered question with random ordered question'''
    capitals_key = list(capitals)
    random.shuffle(capitals_key)

    quiz_file = open(f'capitals_quiz_{quiznum:02d}', 'w')
    quiz_ans_file = open(f'capitals_quiz_ans_{quiznum:02d}', 'w')

    quiz_file.write(
        'Name:\nDate:\nPeriod:\n\n\t\tState Capital Quiz (Form %s)\n\n' % quiznum)
    quiz_ans_file.write(f"''' Key Answer {quiznum:02d}  '''\n\n")

    for num, capital in enumerate(capitals_key):
        question = create_question(num+1, capital)
        quiz_file.write(question)

    quiz_ans_file.write(pprint.pformat(key_ans))
    quiz_file.close()
    key_ans.clear()


def main():
    # create 35 quiz files for each student
    num_student = 35
    for quiznum in range(num_student):
        create_quiz(quiznum+1)


if __name__ == "__main__":
    main()
    # pass
