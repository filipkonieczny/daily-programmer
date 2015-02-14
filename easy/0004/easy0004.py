#!/usr/bin/env python
# encoding: utf-8


# Easy Challenge #4 post:
# http://www.reddit.com/r/dailyprogrammer/comments/pm6oj/2122012_challenge_4_easy/


# imports
from random import choice
from string import letters, digits


# constants
collection = ''.join((letters, digits))


# functions
def validate_int(integer):
    '''
    Determines if received string is a valid integer.

    (string) -> bool

    >>> validate_int('1')
    True

    '''

    try:
        integer = int(integer)
        return True
    except ValueError:
        return False


def get_integer(msg):
    '''
    Gets an integer based on user input.

    (string) -> string

    >>> get_integer('Enter a number: ')
    1

    '''

    while True:
        integer = raw_input(msg)
        if not validate_int(integer):
            print 'Pls, enter a valid integer!\n'
        else:
            return int(integer)


def generate_password(length):
    '''
    Generates a random password of a given length.

    (int) -> string

    >>> generate_password(10)
    '9aERVuMNJA'

    '''

    return ''.join(choice(collection) for i in xrange(length))


def main():
    '''
    Main function taking care of all the logic and human-computer interaction.

    '''

    # 'hello' message
    print '\nOhai! Random password generator - enjoy!\n'

    # main phase
    passwords = get_integer('How many passwords would you like to generate?: ')
    passwords_length = get_integer('And their length?: ')

    print 'There you go, here are your passwords!:\n\n'

    for i in xrange(passwords):
        print generate_password(passwords_length)

    # 'goodbye' message
    print '\n\nThanks for using me!\n'


if __name__ == '__main__':
    main()
