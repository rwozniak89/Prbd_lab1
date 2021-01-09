#!/usr/bin/env python3
"""reducer3.py"""

from operator import itemgetter
import sys
import math   # This will import math module
import numpy as np

current_word = None
current_count = 0
word = None


index = 0
mnozenie_elem = 1
sr_geom = 0
# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input we got from mapper.py
    word, count = line.split('\t', 1)

    # convert count (currently a string) to int
    try:
        count = int(count)
        x = int(word)
    except ValueError:
        # count was not a number, so silently
        # ignore/discard this line
        continue

    mnozenie_elem *= x

    index +=1

if index != 0:
    sr_geom = mnozenie_elem**(1/index)

print(sr_geom)

    # this IF-switch only works because Hadoop sorts map output
    # by key (here: word) before it is passed to the reducer
    #if current_word == word:
    #    current_count += count
    #else:
    #    if current_word:
    #        # write result to STDOUT
    #        print ('%s\t%s' % (current_word, current_count))
    #    current_count = count
    #    current_word = word




# do not forget to output the last word if needed!
#if current_word == word:
#   print ('%s\t%s' % (current_word, current_count))
#
#/usr/local/hadoop/bin/hdfs dfs -cat tutorial/books-streaming-out-pyt3/part-00000
