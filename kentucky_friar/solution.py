#!/usr/bin/env python3
"""Kentucky Friar"""

import argparse
import os
import re


# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Southern fry text',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text', metavar='str', help='Input text or file')

    args = parser.parse_args()

    if os.path.isfile(args.text):
        args.text = open(args.text).read()

    return args


# --------------------------------------------------
def fry(word):
    """
    Drop the 'g' from '-ing' words, change "you" to "y'all"
    """

    ing_word = re.search('(.+)ing$', word)
    you = re.match('([Yy])ou$', word)

    if ing_word:
        prefix = ing_word.group(1)
        if re.search('[aeiouy]', prefix):
            return prefix + "in'"
    elif you:
        return you.group(1) + "'all"

    return word


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    for line in args.text.splitlines():
        print(''.join(map(fry, re.split(r'(\W+)', line.rstrip()))))


# --------------------------------------------------
if __name__ == '__main__':
    main()
