#!/usr/bin/env python
# encoding: utf-8


# Medium Challenge #3 post:
# http://www.reddit.com/r/dailyprogrammer/comments/pkwb1/2112012_challenge_3_intermediate/


# imports
from string import lowercase


# functions
def validate_key(key):
    '''
    Makes sure that key has no repeating letters.

    (string) -> string

    >>> validate_key('hakuna matata')
    'hakunmt'

    '''

    validated_key = [letter.lower() if letter not in key[:i] and letter.lower() in lowercase else '' for i, letter in enumerate(key)]
    return ''.join(validated_key)


def get_cipher(key):
    '''
    Validates the key and creates a cipher based on it.

    (string) -> string

    >>> get_cipher('hakuna matata')
    'hakunmtbcdefgijlopqrsvwxyz'

    '''

    validated_key = validate_key(key)
    cipher = [letter if letter not in validated_key else '' for letter in lowercase]
    return ''.join((validated_key, ''.join(cipher)))


def encode(text, key):
    '''
    Encodes based on received text and key.

    (string, string) -> string

    >>> encode('mary had a little lamb', 'hakuna matata')
    'ghpy bhu h fcrrfn fhga'

    '''

    cipher = get_cipher(key)
    encoded_text = [cipher[lowercase.index(i)] if i in lowercase else i for i in text]
    return ''.join(encoded_text)


def decode(text, key):
    '''
    Decodes based on received text and key.

    (string, string) -> string

    >>> decode('ghpy bhu h fcrrfn fhga', 'hakuna matata')
    'mary had a little lamb'

    '''

    cipher = get_cipher(key)
    decoded_text = [lowercase[cipher.index(i)] if i in cipher else i for i in text]
    return ''.join(decoded_text)


def main():
    '''
    Main function handling human-computer interaction and all logic.

    '''

    # 'hello' message
    print '\nOhai! This is an alphabetical substitution cipher - enjoy!\n'

    phrase = 'mary had a little lamb'
    key = 'hakuna matata'
    encoded = encode(phrase, key)

    print "basic  : '{}'".format(phrase)
    print "encoded: '{}'".format(encoded)
    print "decoded: '{}'".format(decode(encoded, key))

    # 'goodbye' message
    print '\n\nCheers!\n'


if __name__ == '__main__':
    main()
