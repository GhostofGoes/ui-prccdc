#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Original code attributed to Matthew Brown (https://github.com/1BADragon/passgen)

"""passgen.py. A password generator used for PRCCDC.

Usage:
    passgen.py [options]
    passgen.py (-h | --help)
    passgen.py --version

Options:
    -c COUNT    Number of passwords to generate [default: 1]
    -f FILE     Location of word list text file [default: wordlist.txt]
    -m MIN      Minimum length of dictionary word [default: 0]
    -w MAX      Maximum length of dictionary word [default: 100]
    -l LENGTH   Length of Password
    -h, --help  Prints the help
    --version   Prints the current version

"""

from random import randint
from docopt import docopt
from tabulate import tabulate

__version__ = "1.1.0"
args = docopt(__doc__, version=__version__, help=True)
filename = args['-f']
if args['-l']:
    passLength = int(args['-l'])
else:
    passLength = None
wordMax = int(args['-w'])
wordMin = int(args['-m'])
count = int(args['-c'])

if passLength is not None and wordMax < passLength:
    print('Word Max must be larger than passlength')
    exit(1)

symbols = '=+-_/*!@#$%^&*'
print("Symbols being used: %s" % symbols)

try:
    wordList = open(filename)
except FileNotFoundError:
    print(filename + ' does not exist')
    exit(1)
  
data = wordList.read().split('\n')
acceptedList = []

for word in data:
    if wordMin <= len(word) <= wordMax:
        acceptedList.append(word)
  
numWords = 3
if passLength is not None:
    numWords = int(passLength/wordMax + 1)

table = []
for _ in range(count):
    password = ''
    for i in range(numWords):
        word = acceptedList[randint(0, len(acceptedList)-1)]
        password += word + symbols[randint(0, len(symbols)-1)]
    password += str(randint(0, 9999))
    table.append(password)
    print(password)

print(tabulate(table, list(range(0, 10))))
