#!/usr/bin/python

"""
tail clone by Nate Gallagher
with inspiration from
https://gist.github.com/amitsaha/5990310

Usage: tail.py [# LINES] [FILE]
"""

import sys, os, re


nargs = len(sys.argv)
if nargs > 3 or nargs < 2:
    print 'Usage: tail.py [# LINES] [FILE]'
    sys.exit(1)
elif nargs == 2:
    lines = 10      # default
    fname = sys.argv[1]
else:
    try:
        lines = int(sys.argv[1])
    except:
        print '2nd argument must be a number'
        print 'Usage: tail.py [# LINES] [FILE]'
        sys.exit(2)

    fname = sys.argv[2]

try:
    fsize = os.stat(fname).st_size
except:
    print 'No such file or directory:', fname
    print 'Usage: tail.py [# LINES] [FILE]'
    sys.exit(2)

chunk = 256
i = 0
with open(fname) as f:
    if chunk > fsize:
        chunk = fsize - 1
    data = []
    while True:
        i += 1
        f.seek(fsize - chunk * i)
        # regex split by newline but don't remove newline char
        chunklist = re.split('([^\n]+\n)',  f.read(chunk))
        data = chunklist + data
        # twice the lines to account for empty strings in list
        # +i to account for broken lines
        # +1 for luck
        if len(data) >= ((lines*2)+i+1):
            # join split lines from chunks then split file by newline char
            data = ''.join(data).split('\n')
            # print out only needed amount of data list
            print('\n'.join(data[-(lines):]))
            break
