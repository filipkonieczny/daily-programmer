#!/usr/bin/env python
# encoding: utf-8


# Hard Challenge #1 post:
# http://www.reddit.com/r/dailyprogrammer/comments/pii6j/difficult_challenge_1/


# imports
from time import sleep


# globals
MIN_NUMBER = 1
MAX_NUMBER = 1000


# functions
def get_user_input():
    '''
    Gets User input, validates it and returns.

    >>> get_user_input()
    7

    '''

    user_input_msg = "Enter a number({}-{}): ".format(
        MIN_NUMBER,
        MAX_NUMBER
    )

    while True:
        user_input = raw_input(user_input_msg)

        try:
            user_input = int(user_input)

            if not (MIN_NUMBER <= user_input <= MAX_NUMBER):
                print 'Number has to be in range {}-{}!\n'.format(
                    MIN_NUMBER,
                    MAX_NUMBER
                )
                continue
        except ValueError:
            print 'It has to be a number!\n'
        else:
            return user_input


def guess(number):
    '''
    Tries to guess number based on received input.

    >>> guess(7)
    Is this number lower than 500?  Yes.
    Is this number lower than 250?  Yes.
    Is this number lower than 125?  Yes.
    Is this number lower than 63?  Yes.
    Is this number lower than 32?  Yes.
    Is this number lower than 16?  Yes.
    Is this number lower than 8?  Yes.
    Is this number lower than 4?  No.
    Is this number lower than 6?  No.
    Is this number lower than 7?  No.
    It has to be 7 then!!

    '''

    lower_border = MIN_NUMBER
    higher_border = MAX_NUMBER + 1

    while True:
        if higher_border - lower_border == 1:
            print "It has to be {} then!!".format(higher_border - 1)
            break

        current_half = (higher_border + lower_border) / 2
        print 'Is this number lower than {}? '.format(current_half),

        if number < current_half:
            print 'Yes.'
            higher_border = current_half
        else:
            print 'No.'
            lower_border = current_half

        sleep(0.1)


def main():
    '''
    Main function taking care of human-computer interaction,
    as well as executing other functions.

    '''

    # hello message
    print '\nOhai! This is a simple game where computer is trying to guess ' \
          'the number that User has entered. Enjoy!\n'

    # get user input
    number = get_user_input()

    # start guessing
    guess(number)

    # goodbye message
    print '\nKthxbai!\n'


if __name__ == '__main__':
    main()
