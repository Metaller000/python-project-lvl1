#!/usr/bin/env python3
from brain_games import cli
from brain_games import bcore


def main():
    print('Welcome to the Brain Games!')
    name = cli.welcome_user()
    print(f'Hello, {name}')
    print('Find the greatest common divisor of given numbers.')

    cor_flag = True
    for i in bcore.get_range():
        num_first = bcore.get_num()
        num_second = bcore.get_num()
        corr = str(bcore.get_gcd(num_first, num_second))

        print(f'Question: {num_first} {num_second}')
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
