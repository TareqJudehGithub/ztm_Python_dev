from random import randint


class GuessingGame:
    attempts = 3

    def __init__(self):
        self.guessing_func()

    def restart_game(self):
        GuessingGame.attempts = 3

        restart = input('Restart game? (y/n) ').lower()
        if restart == 'y':
            self.guessing_func()

        else:
            print('Good bye!')
            return

    def guessing_func(self):
        random_num = randint(1, 10)

        print(f'No. to guess {random_num}')
        while True:
            try:
                guess = int(input('Guess a number from 1-10: '))
                if guess < 1 or guess > 10:
                    print('Input must be within range')
                    continue

            except ValueError as err:
                print(f'Input must be an integer\n{err}')

            else:
                # winning condition
                if guess == random_num:
                    print(f'Correct! you\'ve guessed {random_num}')
                    return self.restart_game()

                else:
                    # wrong guess, and update attempts left and display it to the user
                    GuessingGame.attempts -= 1
                    print('Wrong guess!')
                    print(f'Remaining attempts = {GuessingGame.attempts}')

                    # ask user to restart game
                    if GuessingGame.attempts == 0:
                        print('Game Over!')
                        return self.restart_game()

                    continue


if __name__ == '__main__':
    GuessingGame()
