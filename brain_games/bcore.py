import random
import prompt


def answer():
    return prompt.string('Your answer: ').lower()


def get_num(num=100):
    return random.randint(1, num)


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
