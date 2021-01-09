#!/usr/bin/env python3
"""reducer3.py"""

from operator import itemgetter
import sys
import math   # This will import math module
import numpy as np

current_word = None
current_count = 0
word = None
maximum = -100000
liczba_elem =0
suma = 0
sr_art = 0
sr_geom = 0
mnozenie_elem = 1
lista = []
zbior = set()
x = 0
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
    print ('%s\t%s' % (x, count))
    if x > maximum:
        maximum = x
    suma += x
    liczba_elem += 1
    mnozenie_elem *= x
    lista.append(x)
    zbior.add(x)

if liczba_elem != 0:
    sr_art = suma / liczba_elem
sr_geom = mnozenie_elem**(1/liczba_elem)

print(f'1. Największą liczbę: {maximum}')
print(f'2. Średnią arytmetyczną: {sr_art}')
print(f'3. Średnią geometryczną {sr_geom}')
print(f'4. Medianę: {np.median(np.array(lista))}')
print(f'5. Liczbę różnych liczb: {len(zbior)}')

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
