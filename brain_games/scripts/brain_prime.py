#!/usr/bin/env python3
from brain_games import cli
from brain_games import bcore


def main():
    print('Welcome to the Brain Games!')
    name = cli.welcome_user()
    print(f'hello, {name}')
    print('Answer "yes" if given number is prime. Otherwise answer "no".')

    cor_flag = True
    for i in bcore.get_range():
        num = bcore.get_num(1, 4000)
        print(f'Question: {num}')
        ans = bcore.answer()

        corr = bcore.check_prime_or_not(num)
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
