import random
import prompt
import math


def answer():
    return prompt.string('Your answer: ').lower()


def get_num(min=0, max=100):
    return random.randint(min, max)


def check_even_or_not(num):
    return 'yes' if num % 2 == 0 else 'no'


def get_operator(operator=['+', '-', '*', '/']):
    return random.choice(operator)


operator_functions = {
    '+': lambda a, b: a + b,
    '-': lambda a, b: a - b,
    '*': lambda a, b: a * b,
    '/': lambda a, b: a / b,
}


def get_calculation(operator=get_operator, num_1=1, num_2=1):
    return operator_functions[operator](num_1, num_2)


def get_range(num=3):
    return range(num)


def get_gcd(num1=1, num2=1):
    return math.gcd(num1, num2)


def gen_progression(min=5, max=10):
    genereted = []
    start_num = get_num(1, 10)
    genereted.append(start_num)
    step = get_num(1, 10)
    for i in get_range(get_num(min, max) - 1):
        start_num = start_num + step
        genereted.append(start_num)
    return genereted


def get_progression():
    progression = gen_progression()
    hide_num = random.choice(progression)
    progression_str = ''
    for num in progression:
        if hide_num == num:
            progression_str = progression_str + '.. '
        else:
            progression_str = progression_str + f'{num} '
    return [hide_num, progression_str]
