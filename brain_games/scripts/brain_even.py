#!/usr/bin/env python3
from brain_games import cli
import random
import prompt


def answer():
    return prompt.string('Your answer: ').lower()


def get_num(num=100):
    return random.randint(1, num)


def check_even_or_not(num):
    return 'yes' if num % 2 == 0 else 'no'


def main():
    print('Welcome to the Brain Games!')
    name = cli.welcome_user()
    print(f'hello, {name}')
    print('Answer "yes" if the number is even, otherwise answer "no".')

    cor_flag = True
    for i in '123':
        num = get_num()
        print(f'Question: {num}')
        cor = check_even_or_not(num)
        ans = answer()
        if cor != ans:
            print(f"'{ans}' is wrong answer ;(. Correct answer was '{cor}'.")
            print(f"Let's try again, {name}!")
            cor_flag = False
            break
        else:
            print('Correct!')

    if cor_flag:
        print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()
