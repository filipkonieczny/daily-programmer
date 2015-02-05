#!/usr/bin/env python
# encoding: utf-8


# Easy Challenge #2 post:
# http://www.reddit.com/r/dailyprogrammer/comments/pjbj8/easy_challenge_2/


# constants
COMMANDS = ('f', 'm', 'a')
AVAILABLE_COMMANDS = '/'.join(COMMANDS)


# functions
def _get_user_input(msg, expected_input, error_msg=None):
    '''
    Gets user input in a while loop, designed to be used by other functions.

    (string, string, (strings)) -> string

    >>> _get_user_input('You okay?(y/n): ', ('y', 'n'))
    'y'

    '''

    if error_msg is None:
        error_msg = 'Oops, looks like input was incorrect!\n'

    while True:
        user_input = raw_input(msg)
        user_input = user_input.lower()

        if user_input not in expected_input:
            print error_msg
        else:
            return user_input


def get_command():
    '''
    Gets command using _get_user_input() internal function.

    >>> get_command()
    'f'

    '''

    command = _get_user_input(
        'Which of the following would you like to calculate?({}): '.format(
            AVAILABLE_COMMANDS
        ),
        COMMANDS
    )
    return command


def _validate_float(number):
    '''
    Validates if a number is a float.

    (string) -> bool

    >>> _validate_float('1.0')
    True

    '''

    try:
        number = float(number)
        return True
    except ValueError:
        return False


def _get_value(symbol):
    '''
    Gets value, validates it using _validate_float()

    >>> _get_value('F')
    1.0

    '''

    while True:
        input_value = raw_input('Input {} value: '.format(symbol))

        if not _validate_float(input_value):
            print 'Please enter a number!\n'
        else:
            return float(input_value)


def get_values(command):
    '''
    Gets values for all symbols and returns them.

    (string) -> dict

    >>> get_values()

    '''

    if command != 'f':
        f_value = _get_value('F')
    else:
        f_value = 0

    if command != 'm':
        m_value = _get_value('M')
    else:
        m_value = 0

    if command != 'a':
        a_value = _get_value('A')
    else:
        a_value = 0

    data = {
        'f': f_value,
        'm': m_value,
        'a': a_value
    }

    return data


def execute_command(command, values):
    '''
    Performs calculation based on passed command and values.

    (string, dict) -> float

    >>> execute_command('f', {'f': 0, 'm': 2.0, 'a': 3.0})
    6.0

    '''

    f_value = values['f']
    m_value = values['m']
    a_value = values['a']

    if command == 'f':
        print 'F = {}'.format(m_value * a_value)
    elif command == 'm':
        print 'M = {}'.format(f_value * a_value)
    else:
        print 'A = {}'.format(f_value / m_value)


def get_continuation():
    '''
    Asks the User if wants to continue.

    () -> bool

    >>> get_continuation()
    True

    '''

    continuation = _get_user_input(
        '\nWould you like to continue?(y/n): ',
        ('y', 'n')
    )

    if continuation == 'y':
        return True
    return False


def main():
    '''
    Main function taking care of all the logic and human-computer interaction.

    '''

    # 'hello' message
    print '\nOhai! Calculate F = M * A and its variants accrodingly. Enjoy!\n'

    # main phase
    while True:
        command = get_command()
        values = get_values(command)
        execute_command(command, values)

        if not get_continuation():
            break

    # 'goodbye' message
    print '\n\nThanks for using me!\n'


if __name__ == '__main__':
    main()
