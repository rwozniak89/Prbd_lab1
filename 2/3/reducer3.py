#!/usr/bin/env python3
"""reducer3.py"""

from operator import itemgetter
import sys

import pandas as pd

current_word = None
current_count = 0
word = None
current_bigram = None
index =0
lista = []
lista_ost = []
# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input we got from mapper.py
    
    word, count, word2 = line.split('\t', 2)
    #print(word)
    #print(word2)
    index += 1
    #if index > 5 :
    #    break
    # convert count (currently a string) to int
    try:
        count = int(count)
    except ValueError:
        # count was not a number, so silently
        # ignore/discard this line
        continue

    # this IF-switch only works because Hadoop sorts map output
    # by key (here: word) before it is passed to the reducer
 
 
    if current_word == word:
        current_count += count
        lista.append([current_bigram])
        current_bigram = f'({word} {word2})'

    else:
        lista.append([current_bigram])
        if current_word:
            # write result to STDOUT
            print ('(%s *) %s' % (current_word, current_count))
            ar = pd.DataFrame(lista)
            procenty = ar.value_counts(normalize=True)
            index_p = 0
            for p in procenty:
                zwrot = str(lista[index_p]).replace("['", "").replace("']", "")
                if p == 1:
                    print(f'{zwrot} 1')
                else:
                    print(f'{zwrot} {round(p,3)}')
                index_p += 1
                   
        current_count = count
        current_word = word
        current_bigram = f'({word} {word2})'
        lista_ost = lista.copy()
        lista = [] 
        print('')
    
        

# do not forget to output the last word if needed!
if current_word == word:
    print ('(%s *) %s' % (current_word, current_count))
    lista = lista_ost.copy()
    ar = pd.DataFrame(lista)
    procenty = ar.value_counts(normalize=True)
    index_p = 0
    for p in procenty:
        zwrot = str(lista[index_p]).replace("['", "").replace("']", "")
        if p == 1:
            print(f'{zwrot} 1')
        else:
            print(f'{zwrot} {round(p,3)}')
        index_p += 1

