import sys
from random import randint

# Build a guessing game 1 - 10

# instantiate two variables which will serve as randint function arguments
user_input = sys.argv[1]

attempts = 3
num_to_guess = randint(1, 10)
print(f'Number to guess: {num_to_guess}')

while True:
    try:
        guess = int(input('Guess a number 1-10: '))
        print(guess)
        print(f'Attempts left: {attempts}')
        if 1 <= guess <= 10:
            print('All good!')
        else:
            print('Your input should be between the numbers 1 - 10')
            continue

    except ValueError as err:
        print(f'Your input should only be an integer.\n {err}')
        continue

    else:
        if num_to_guess == guess:
            print(f'Congratulations!\nYou\'ve got the correct number! which is {num_to_guess}')
        else:
            attempts -= 1
            print('Oh well.. you guessed it wrong this time.. but don\'t give up!')
            print(f'Attempts left: {attempts}')

            if attempts == 0:
                print('Game Over! Good Bye!')

                play_again = input('Play again? (y/n) ').lower()
                if play_again == 'y':
                    attempts = 3
                    continue

                else:
                    print('Good Bye!')
                    break
