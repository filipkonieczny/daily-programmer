#!/usr/bin/env python
# encoding: utf-8


# Hard Challenge #3 post:
# http://www.reddit.com/r/dailyprogrammer/comments/pkwgf/2112012_challenge_3_difficult/


# globals
WORDS_FILE = 'words.txt'
scrambled_words = [
    'mkeart',
    'sleewa',
    'edcudls',
    'iragoge',
    'usrlsle',
    'nalraoci',
    'nsdeuto',
    'amrhat',
    'inknsy',
    'iferkna'
]


# functions
def load_file(file=WORDS_FILE):
    '''
    Load the 'words.txt' file, return list of words with trimmed newline.

    (string) -> [strings]

    >>> load_file()
    ['html:)', ..., 'sports']

    '''

    with open(WORDS_FILE, 'r') as outfile:
        words = outfile.readlines()
        for i, word in enumerate(words):
            words[i] = word[:-1]
        return words


def main():
    '''
    Main function taking care of human-computer interaction.

    '''

    # hello message
    print '\nOhai! This is a simple word unscrambling script - enjoy!\n'

    # load the words file
    words = load_file()

    # unscramble the words
    for scrambled_word in scrambled_words:
        matches = [word for word in words if sorted(word) == sorted(scrambled_word)]
        print '{} stands for: {}'.format(scrambled_word, ','.join(matches))

    # goodbye message
    print '\nKthxbai!\n'


if __name__ == '__main__':
    main()
