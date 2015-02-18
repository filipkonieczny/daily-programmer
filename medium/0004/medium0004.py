#!/usr/bin/env python
# encoding: utf-8


# Medium Challenge #4 post:
# http://www.reddit.com/r/dailyprogrammer/comments/pm6sq/2122012_challenge_4_intermediate/


# globals
operators = {
    '+': lambda a, b: a + b,
    '-': lambda a, b: a - b,
    '*': lambda a, b: a * b,
    '/': lambda a, b: a / b
}


# functions
def validate_input(user_input):
    '''
    Validates user input, checks if it doesn't contain any
    *undesirable* characters, if there aren't any operators
    at the beginning/end or if operators aren't followed
    by another operators.

    (string) -> bool

    >>> validate_input('2+2')
    True

    '''

    # check if it's empty
    if not user_input:
        return None

    # check if there aren't any invalid characters
    for i in user_input:
        try:
            i = int(i)
        except ValueError:
            if i not in operators:
                print "Oops, '{}' is an invalid character!!\n".format(i)
                return False

    # check if there aren't operators at the beginning/end
    if user_input[0] in operators or user_input[-1] in operators:
        print "There can't be an operator at the beginning/ending!!\n"
        return False

    # check if any operator isn't followed by another operator
    for i in xrange(1, len(user_input)):
        if user_input[i - 1] in operators and user_input[i] in operators:
            print "Wat? Operators can't be right next to each other!\n"
            return False
    return True


def get_input():
    '''
    Gets user input and makes sure it's valid with validate_input().

    () -> string

    >>> get_input()
    '2+2'

    '''

    while True:
        user_input = raw_input('>>> ')

        validated_input = validate_input(user_input)
        if validated_input is None:
            return None

        if validated_input:
            return user_input


def strip_user_input(user_input):
    '''
    Strips user_input into segments of numbers and operators.

    (string) -> [floats, strings]

    >>> stripped_user_input('2+2')
    [2.0, '+', 2.0]

    '''

    start = 0
    stripped_user_input = []

    for i, char in enumerate(user_input):
        if char in operators:
            stripped_user_input.append(float(user_input[start:i]))
            stripped_user_input.append(char)
            start = i + 1
    stripped_user_input.append(float(user_input[start:]))

    return stripped_user_input


def evaluate_operation(stripped_user_input, operator):
    '''
    Discovers an operation and evaluates it.

    ([floats, strings], string) -> [floats, strings]

    >>> evaluate_operation([2.0, '+', 2.0], '+')
    [4.0]

    '''

    if operator in stripped_user_input:
        current = stripped_user_input.index(operator)
        current_result = operators[operator](
            stripped_user_input[current - 1],
            stripped_user_input[current + 1]
        )
        stripped_user_input[current - 1] = current_result
        stripped_user_input.pop(current)
        stripped_user_input.pop(current)
    return stripped_user_input


def evaluate(user_input):
    '''
    Evaluates the whole sequence.

    (string) -> float

    >>> evaluate('2+2')
    4.0

    '''

    stripped_user_input = strip_user_input(user_input)

    while stripped_user_input:
        stripped_user_input = evaluate_operation(stripped_user_input, '*')
        stripped_user_input = evaluate_operation(stripped_user_input, '/')
        stripped_user_input = evaluate_operation(stripped_user_input, '+')
        stripped_user_input = evaluate_operation(stripped_user_input, '-')

        if len(stripped_user_input) == 1:
            break
    return stripped_user_input[0]


def main():
    '''
    Main function handling human-computer interaction and all logic.

    '''

    # 'hello' message
    print '\nOhai! This is a simple calculator implementation - enjoy!\n'

    # main logic
    while True:
        user_input = get_input()
        if user_input is None:
            break
        print '  = {}\n'.format(evaluate(user_input))

    # 'goodbye' message
    print '\n\nCheers!\n'


if __name__ == '__main__':
    main()
