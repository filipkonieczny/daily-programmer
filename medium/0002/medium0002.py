#!/usr/bin/env python
# encoding: utf-8


# Medium Challenge #2 post:
# http://www.reddit.com/r/dailyprogrammer/comments/pjbuj/intermediate_challenge_2/


# imports
from random import randint


# globals
DIRECTIONS = ('n', 'e', 'w', 's')


# functions
def get_name():
    '''
    Asks the Hero for the name.

    >>> get_name()
    'jhgrng'

    '''

    while True:
        name = raw_input("What's your name, hero?: ")

        if not name:
            print 'Pls, hero, enter a name...\n'
        else:
            return name


def get_direction():
    '''
    Asks the Hero for a direction.

    >>> get_direction()
    'n'

    '''

    while True:
        direction_text = "Where would you like to go?({}): "
        direction = raw_input(direction_text.format('/'.join(DIRECTIONS)))
        direction = direction.lower()

        if direction not in DIRECTIONS:
            print 'Pls, hero, enter a direction...\n'
        else:
            print "You go {}, and you encounter...".format(direction.upper())
            return direction


def encounter(health):
    '''
    Performs an encounter upon making a move and calculates health afterwards.

    >>> encounter(1)
    0

    '''

    random_encounter = randint(1, 10)

    if random_encounter == 10:
        print 'Nothing! Phew, that was a close one!\n'
    elif random_encounter <= 9 and random_encounter >= 6:
        health += 1
        print 'A potion! Raises your health to: {}!\n'.format(health)
    else:
        health -= randint(1, 2)
        print 'An enemy! You kill it, but it harms you too!'

        if health < 0:
            health = 0
        print 'You now have {} health left!\n'.format(health)
    return health


def main():
    '''
    Main function handling human-computer interaction and all logic.

    '''

    # 'hello' message
    print '\nOhai! This is a simple text adventure - enjoy!\n'

    # setup
    name = get_name()
    health = 10
    moves = 0

    print "\n\nAlright, {}, let's go on an adventure!!\n\n".format(name)
    print "You find yourself in a deep forest, lost..."

    while True:
        get_direction()
        health = encounter(health)

        moves += 1

        if not health:
            print '\nOops, you died...\n'
            break

    print 'Congratulations on making {} moves though!'.format(moves)

    # 'goodbye' message
    print '\n\nCheers!\n'


if __name__ == '__main__':
    main()
