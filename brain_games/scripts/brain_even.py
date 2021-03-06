#!/usr/bin/env python3
from brain_games import cli
from brain_games import bcore


def main():
    print('Welcome to the Brain Games!')
    name = cli.welcome_user()
    print(f'Hello, {name}')
    print('Answer "yes" if the number is even, otherwise answer "no".')

    cor_flag = True
    for i in bcore.get_range():
        num = bcore.get_num()
        print(f'Question: {num}')
        cor = bcore.check_even_or_not(num)
        ans = bcore.answer()
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
