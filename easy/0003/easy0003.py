#!/usr/bin/env python
# encoding: utf-8


# Easy Challenge #3 post:
# http://www.reddit.com/r/dailyprogrammer/comments/pkw2m/2112012_challenge_3_easy/


# imports
from string import lowercase, uppercase


# constants
LETTERS_LENGTH = len(lowercase)


# functions
def caesar_cypher(text, jump, direction):
    '''
    Caesar Cypher implementation.

    (string, int, int) -> string

    >>> caesar_cypher('Mary had a little lamb.', 49, 1)
    'Jxov exa x ifqqib ixjy.'

    '''

    caesar_jump = jump % LETTERS_LENGTH * direction
    caesared_text = ''

    for letter in text:
        if letter == letter.upper():
            letters = uppercase
        else:
            letters = lowercase

        if letter in letters:
            jump_index = letters.index(letter) + caesar_jump
            caesared_letter_index = jump_index % LETTERS_LENGTH
            caesared_letter = letters[caesared_letter_index]
        else:
            caesared_letter = letter

        caesared_text = ''.join((caesared_text, caesared_letter))

    return caesared_text


def cypher(text, jump):
    '''
    caesar_cypher() implementation with a positive direction.

    '''

    return caesar_cypher(text, jump, 1)


def decypher(text, jump):
    '''
    caesar_cypher() implementation with a negative direction.

    '''

    return caesar_cypher(text, jump, -1)


def main():
    '''
    Main function taking care of all the logic and human-computer interaction.

    '''

    # 'hello' message
    print '\nOhai! Casear cypher!\n'

    # main phase
    phrase = 'Mary had a little lamb.'
    cypher_jump = 49
    cyphered = cypher(phrase, cypher_jump)
    decyphered = decypher(cyphered, cypher_jump)

    print 'start: {}'.format(phrase)
    print 'cyphered: {}'.format(cyphered)
    print 'decyphered: {}'.format(decyphered)

    # 'goodbye' message
    print '\n\nThanks for using me!\n'


if __name__ == '__main__':
    main()
