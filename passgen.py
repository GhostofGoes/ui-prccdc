#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Derived from passgen.by by Matthew Brown. (https://github.com/1BADragon/passgen)
# Author:   Christopher Goes
# Email:    goes8945@vandals.uidaho.edu
# Repo:     https://github.com/GhostofGoes/ui-prccdc

"""passgen.py. A password generator used for University of Idaho for PRCCDC.
Tabulate is used for formatting, full reference here: https://pypi.python.org/pypi/tabulate
I recommend redirecting the output to a file with the appropriate extension.

Usage:
    passgen.py [options]
    passgen.py (-h | --help)
    passgen.py --version

Options:
    -r ROWS         Number of rows of passwords to generate [default: 5]
    -c COLS         Number of columns of passwords to generate [default: 5]
    -m MIN          Minimum length of a dictionary word [default: 4]
    -w MAX          Maximum length of a dictionary word [default: 4]
    -f FILE         Location of word list text file [default: wordlist.txt]
    -l LENGTH       Number of words to use in a password [default: 3]
    -t FORMAT       Format to use for Tabulate (latex | orgtbl | plain | html) [default: orgtbl]
    -h, --help      Prints the help
    --version       Prints the current version

"""

from random import shuffle, randint
from docopt import docopt
from tabulate import tabulate

__version__ = "2.1.0"
args = docopt(__doc__, version=__version__, help=True)


# Get the word list from a file
with open(args['-f'], 'r') as wordfile:
    data = wordfile.read().split('\n')

wordMax = int(args['-w'])
wordMin = int(args['-m'])
if wordMin > wordMax:
    print("(ERROR) Minimum wordsize %d must be less than maximum wordsize %d" % (wordMin, wordMax))
    exit(1)

rows = int(args['-r'])
cols = int(args['-c'])
numWords = int(args['-l'])
assert rows > 0
assert cols > 0
assert numWords > 0

symbols = '=+-_/*!@#$%^&*'
print("Symbols being used: %s\n" % symbols)


# Generate a list of words to use from the shuffled word file
acceptedList = []
shuffle(data)
for word in data:
    if wordMin <= len(word) <= wordMax:
        acceptedList.append(word)


# Build the table as a list of lists
table = []
for c in range(1, rows + 1):
    row = [c]               # Set the first column in a row to the row number
    for _ in range(cols):   # Generates passwords for the row
        password = ''
        for i in range(numWords):  # Generates a password
            word = acceptedList[randint(0, len(acceptedList)-1)]    # Random word
            password += word + symbols[randint(0, len(symbols)-1)]  # Random symbol
        password += str(randint(0, 10))  # Append a single random integer to end of password
        row.append(password)  # Add password to the row
        # TODO: fixed length passwords using padding (for "prettyness")
    table.append(row)  # Add row to the table

# Print the password table (If you need file output, just redirect on the command line)
headers = list(range(1, cols + 1))  # Column headers
tabulate_format = str(args['-t'])   # Format to use for Tabulate
print(tabulate(table, headers=headers, tablefmt=tabulate_format))
