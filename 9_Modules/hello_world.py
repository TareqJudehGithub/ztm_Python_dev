import sys
from random import randint
# we can access .argv by index number
first_name = sys.argv[1]
last_name = sys.argv[2]

# [0] returns the script name
print(f'Hello, {first_name} {last_name}!')

# In Terminal, run the script name along with arguments for first_name and last_name.


# Build a guessing game 1 - 10


# instantiate two variables which will serve as randint function arguements
user_input = sys.argv[1]


# build a function that generates a random integer:
def guessing_game(user_answer):
    attempts = 3
    num_to_guess = randint(1, 10)
    while True:
        if user_answer == num_to_guess:
            return f'Congratulations!\nYou\'ve got the correct number! which is {num_to_guess}'
        else:
            attempts -= 1
            print('Oh well.. you guessed it wrong this time..\n But don\' give up!')
            print(f'Attempts left: {attempts}')
            print(attempts)
        if attempts == 0:
            return 'No more tries left. Good buy!'


guessing_game(user_input)

# if __name__ == '__name__':
#     user_input = int(input())
#     print(guessing_game(start_int, end_int))
