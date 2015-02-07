#!/usr/bin/env python
# encoding: utf-8


# Hard Challenge #2 post:
# http://www.reddit.com/r/dailyprogrammer/comments/pjsdx/difficult_challenge_2/


# imports
from time import time


# functions
def main():
    '''
    Main function taking care of human-computer interaction.

    '''

    # hello message
    print '\nOhai! This is a simple stopwatch - enjoy!\n'

    while True:
        user_input = raw_input('>>> start: ')
        start_time = time()
        user_input = raw_input('>>> finish: ')

        print 'Time taken: {}\n'.format(time() - start_time)

        if user_input:
            break

    # goodbye message
    print '\nKthxbai!\n'


if __name__ == '__main__':
    main()
