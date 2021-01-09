#!/usr/bin/env python3
"""mapper3.py"""

import sys
import re


words_all = []
# input comes from STDIN (standard input)
for line in sys.stdin:
#for line in test:
    # remove leading and trailing whitespace
    line = line.strip()
    #zmiana all na male litery
    line = line.lower()
    # split the line into words
    #words = re.findall(r'[a-zA-Z]+', line)
    words = re.findall(r'\w+', line)
    words_all += words


index = 0
last_index = len(words_all) - 1
#bigrams = []
for x in words_all:
    if(index < last_index):
        #bigrams.append([words_all[index], words_all[index+1]])
        #print ('(%s %s)' % (words_all[index], words_all[index+1]))
        #print ('%s\t%s' % (words_all[index], words_all[index+1]))
        print ('%s\t%s\t%s' % (words_all[index], 1, words_all[index + 1]))
    index += 1
#print (f'{bigrams}')
    