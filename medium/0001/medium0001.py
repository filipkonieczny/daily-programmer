#!/usr/bin/env python
# encoding: utf-8


# Medium Challenge #1 post:
# http://www.reddit.com/r/dailyprogrammer/comments/pihtx/intermediate_challenge_1/

# imports
import json
import random
import string


# globals
COMMANDS = ('add', 'events', 'edit', 'delete', 'quit')
DATA_FILE = 'data.json'
HASH_PATTERN = ''.join((string.letters, string.digits))
HASH_COMPLEXITY = 2  # the bigger the number, the more unique calendar entries


# classes
class Calendar():
    '''
    Calendar class. Executes commands received and performs any
    neccessary actions.

    '''

    def __init__(self, data):
        '''
        Calendar class constructor, takes only data,
        a dictionary containing all events information.

        '''

        self.data = data
        self.ADD_EVENT_MSG = 'Enter the {} for your event: '

    def _get_event(self):
        '''
        Prompt User to enter event_id - react if such doesn't exist.

        '''

        while True:
            event_id = raw_input('Enter event ID: ')

            if event_id not in self.data.keys():
                print 'Oops, looks like there are no such events!'

                while True:
                    again = raw_input('Do you wish to continue(y/n)?: ')

                    if again not in ('y', 'n'):
                        print 'Please answer correctly.'
                    else:
                        break

                if again == 'n':
                    break

                continue
            break

        return event_id

    def _add_value(self, event_property):
        '''
        Prompt User to enter a value and then return it.

        '''

        while True:
            value = raw_input(self.ADD_EVENT_MSG.format(event_property))
            if value:
                return value

    def execute_command(self, command):
        '''
        Triggers appropriate funtion based on received command.

        '''

        if command == 'add':
            self.add()
        elif command == 'events':
            self.events()
        elif command == 'edit':
            self.edit()
        else:
            self.delete()

    def add(self):
        '''
        Add event to Calendar.

        '''

        # generate unique id
        while True:
            event = generate_hash()
            if event not in self.data.keys():
                break

        name = self._add_value('name')
        date = self._add_value('date')
        time = self._add_value('time')

        self.data[event] = {
            'name': name,
            'date': date,
            'time': time
        }

    def events(self):
        '''
        Display all current events.

        '''

        if not self.data:
            print 'Oops, there are no events!'
            print "How about entering some with 'add' commands?\n"
            return

        for i in self.data.keys():
            name = self.data[i]['name']
            date = self.data[i]['date']
            time = self.data[i]['time']
            print '{}: {}, {} at {}.'.format(i, name, date, time)

    def edit(self):
        '''
        Edit an event based on its name.

        '''

        event = self._get_event()

        while True:
            name = self.data[event]['name']
            date = self.data[event]['date']
            time = self.data[event]['time']

            data = {
                'name': name,
                'date': date,
                'time': time
            }

            print 'Event: {}, {} at {}.'.format(name, date, time)

            for i in data.keys():
                print 'Event {}: {}'.format(i, data[i])
                while True:
                    new_value = raw_input('Edit or leave blank: ')

                    if new_value:
                        self.data[event][i] = new_value
                    break
            break

    def delete(self):
        '''
        Delete event from Calendar.

        '''

        event = self._get_event()
        self.data.pop(event)


# functions
def generate_hash(pattern=HASH_PATTERN, complexity=HASH_COMPLEXITY):
    '''
    Generates a string with random characters to resemble a simple hash.

    (string, integer) -> string

    >>> generate_hash()
    'h3'

    '''

    return ''.join([random.choice(pattern) for i in xrange(complexity)])


def load_data():
    '''
    Loads any JSON data. If there's no data file,
    or data is corrupted, returns an empty dictionary.

    '''

    try:
        with open(DATA_FILE, 'r') as outfile:
            return json.loads(outfile)
    except (IOError, TypeError):
        return {}


def get_command():
    '''
    Gets commands. Checks if they're valid, meaning that they
    are one of globally defined COMMANDS.

    >>> get_command()
    'add'

    '''

    valid_choices = '/'.join(COMMANDS)

    while True:
        command = raw_input('>>> ')

        if command.lower() not in COMMANDS:
            print 'Please enter a valid command({}).\n'.format(valid_choices)
        else:
            return command


def save_data(data):
    '''
    Saves any JSON data into a file.

    '''

    with open(DATA_FILE, 'w') as outfile:
        json.dump(data, outfile, indent=4)

    print "Data saved into '{}'!".format(DATA_FILE)


def main():
    '''
    Main function handling human-computer interaction, loading/saving data,
    as well as triggering Calendar actions.

    '''

    # 'hello' message
    print '\nOhai! This is a simple calendar app. Have fun!\n'

    # load data and create calendar instance
    data = load_data()
    calendar = Calendar(data)
    del data

    # get commands
    while True:
        command = get_command()

        if command == 'quit':
            break

        calendar.execute_command(command)

    # save data
    data = calendar.data
    save_data(data)

    # 'goodbye' message
    print '\n\nCheers!\n'


if __name__ == '__main__':
    main()
