#!/usr/bin/env python3
"""mapper3.py"""

import sys
import re

# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    #zmiana all na male litery
    line = line.lower()
    # split the line into words
    #words = re.findall(r'[a-zA-Z]+', line)
    words = re.findall(r'\w+', line)
    #words = line.split()
    # increase counters
    for word in words:
        # write the results to STDOUT (standard output);
        # what we output here will be the input for the
        # Reduce step, i.e. the input for reducer.py
        #
        # tab-delimited; the trivial word count is 1
        print ('%s\t%s' % (word, 1))
#
#/usr/local/hadoop/bin/hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.8.2.jar -file /home/$USER/mapper3.py -mapper /home/$USER/mapper3.py -file /home/$USER/reducer3.py -reducer /home/$USER/reducer3.py -input tutorial/books -output tutorial/books-streaming-out-python/
