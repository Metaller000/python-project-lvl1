#!/usr/bin/env python3
from brain_games import cli
from brain_games import bcore


def main():
    print('Welcome to the Brain Games!')
    name = cli.welcome_user()
    print(f'Hello, {name}')
    print('What number is missing in the progression?')

    cor_flag = True
    for i in bcore.get_range():
        progression = bcore.get_progression()
        corr = str(progression[0])

        print(f'Question: {progression[1]}')
        ans = bcore.answer()
        if corr != ans:
            print(f"'{ans}' is wrong answer ;(. Correct answer was '{corr}'.")
            print(f"Let's try again, {name}!")
            cor_flag = False
            break
        else:
            print('Correct!')

    if cor_flag:
        print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()
