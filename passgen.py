#!/usr/bin/env python3
# Original code attributed to Matthew Brown (https://github.com/1BADragon/passgen)

"""passgen.py

Usage:
    passgen.py [options]

Options:
    -c COUNT    Number of passwords to generate [default: 1]
    -f FILE     Location of word list text file [default: wordlist.txt]
    -m MIN      Minimum length of dictionary word [default: 0]
    -w MAX      Maximum length of dictionary word [default: 100]
    -l LENGTH   Maximum length of Password
    -h, --help  Prints the help

"""

from random import randint
from docopt import docopt
from tabulate import tabulate

args = docopt(__doc__)
filename = args['-f']
passLength = int(args['-l'])
wordMax = int(args['-w'])
wordMin = int(args['-m'])
count = int(args['-c'])

if passLength is None and wordMax is None and wordMax > passLength:
    print('Word Max must be larger than passlength')
    exit(1)

symbols = '=+-_/*!@#$%^&*'

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
if passLength is None:
    numWords = int(passLength/wordMax + 1)

table = []
for _ in range(count):
    password = ''
    for i in range(numWords):
        word = acceptedList[randint(0, len(acceptedList)-1)]
        password += word + symbols[randint(0, len(symbols)-1)]
    password += str(randint(0, 9999))
    table.append(password)
    # print(password)

print(tabulate(table, list(range(0, 10))))
