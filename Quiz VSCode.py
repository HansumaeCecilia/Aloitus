# Simple multiple choice quiz using the zip method of listing

import time #Import time to use sleep-function

input('Press ENTER to start')
print()
print('Let\'s begin!')
time.sleep(2) # Moves on from 'Let's begin!' after two seconds
print()

# 5 trivia questions
questions = ['What is the capital of Japan?', 
            'How deep is the Mariana Trench(km)?', 
            'Which year was the United States founded?', 
            'Which year did World War II begin?']

# Multiple choice answer suggestions
answer_choices = ['a) Paris\nb) Tokyo\nc) Stockholm\n:',
                 'a) 850 km\nb) 3,480 km\nc) 2,550 km\n:',
                 'a) 1546\nb) 1801\nc) 1776\n:',
                 'a) 1939\nb) 1899\nc) 1967\n:']

# Correct choices, both the multiple choice characters (a, b, c) and the answer typed out are valid
correct_choices = [{'b', 'Tokyo', 'tokyo'},
                  {'c', '2,550 km', '2,550', '2550'},
                  {'c', '1776'},
                  {'a', '1939'}]

# Correct answers, only printed if the answer is wrong, otherwise 'Correct!' is printed
answers = ['The capital of Japan is Tokyo',
          'The Mariana Trench is 2,550 km deep',
          'The Unitated States was founded in 1776',
          'World War II began in 1939']

# Defining functions for the quiz
def quiz():
    score = 0
    for question, choices, correct_choice, answer in zip (questions, answer_choices, correct_choices, answers):
        print(question)
        player_answer = input(choices).lower()
        if player_answer in correct_choice:
            print('Correct!', 'Your score is:', score, 'out of 4', '\n')
            score += 1 # If the answer is correct, add a point to the score
        else:            
            print('Incorrect.', answer, 'Your score is:', score, 'out of 4', '\n')

if __name__ == "__main__":
    quiz()