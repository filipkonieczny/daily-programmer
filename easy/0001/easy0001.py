#!/usr/bin/env python
# encoding: utf-8


# Easy Challenge #1 post:
# http://www.reddit.com/r/dailyprogrammer/comments/pih8x/easy_challenge_1/


# imports
import json
from datetime import datetime


# constants
INPUT_ERROR_MSG = "\nPlease answer the question.\n"


# functions
def get_string(msg):
    '''
    Gets an answer after asking a question.

    (string) -> string

    >>> get_string("What's your name?: ")
    John

    '''

    while True:
        user_input = raw_input(msg)

        if not user_input:
            print INPUT_ERROR_MSG
        else:
            return user_input


def get_int(msg):
    '''
    Asks a question using get_string() and validates it,
    so that the outcome is always an integer.

    (string) -> integer

    >>> get_string("How old are you?: ")
    18

    '''

    while True:
        try:
            user_input = get_string(msg)
            user_input = int(user_input)

            return user_input
        except ValueError:
            print INPUT_ERROR_MSG


def save_data(file_name, data):
    '''
    Saves any JSON data into a file.

    '''

    with open(file_name, 'w') as outfile:
        json.dump(data, outfile, indent=4)


def main():
    '''
    Main function taking care of all the logic and human-computer interaction.

    '''

    # 'hello' message
    print '\nOhai!\n'

    # get data
    name = get_string("What's your name?: ")
    age = get_int("How old are you?: ")
    username = get_string("What's your username?: ")

    # print data
    print "\nYour name is: {},".format(name)
    print "You're {} years old,".format(age)
    print "Your username is: {}.\n".format(username)

    # save data
    save_date = str(datetime.now()).split('.')[0]
    file_name = '{}.json'.format(save_date)
    directory = '{}'.format(file_name)
    data = {
        'name': name,
        'age': age,
        'username': username
    }
    save_data(directory, data)

    # 'goodbye' message
    print '\nKthxbai!\n'

if __name__ == '__main__':
    main()
