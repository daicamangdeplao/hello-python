import random


def run():
    guessing_round = 0
    while True:
        guessing_round = guessing_round + 1
        user_input = input('Enter a number: ')
        random_number = random.randint(1, 5)
        print(f'Correct number is: {random_number}')

        if int(user_input) == random_number:
            print(f'Congratulation! You win the game after {guessing_round} times of guessing.')
            break


if __name__ == '__main__':
    run()
