#https://mrjob.readthedocs.io/
from mrjob.job import MRJob
import re

from mrjob.step import MRStep
import numpy as np
import pandas as pd

from mrjob.protocol import RawProtocol

WORD_RE = re.compile(r"\w+")
## plus 6 zadań z dodaną wielostopniowością gdzie trzeba i z wykluczeniami: 1. największa liczba; 2 średnia arytmetyczna; 3 średnia geometryczna; 4  mediana; 5 liczba cyfr;
#
# 6 BIGRAMY

# odpalanie  C:\Users\Radek\AppData\Local\Programs\Python\Python39\python.exe mr_3.py inputTest2.txt
class MRWordCount(MRJob):
    FILES = ['stop_words.txt']
    OUTPUT_PROTOCOL = RawProtocol
    def configure_args(self):
        super(MRWordCount, self).configure_args()

        # allow for alternate stop words file
        self.add_file_arg(
            '--stop-words-file',
            dest='stop_words_file',
            default=None,
            help='alternate stop words file. lowercase words, one per line',
        )

    def mapper_init(self):
        stop_words_path = self.options.stop_words_file or 'stop_words.txt'

        with open(stop_words_path) as f:
            self.stop_words = set(line.strip() for line in f)

    def mapper(self, _, line):
        for word in WORD_RE.findall(line):
            try:
                yield(1, word)
            except:
                pass


    def combiner(self, key, values):
        items, summ = 0, 0
        words_all = []

        for value in values:
            items += 1
            words_all.append(value)

        index = 0
        last_index = len(words_all) - 1
        # bigrams = []
        for x in words_all:
            if (index < last_index):
                # bigrams.append([words_all[index], words_all[index+1]])
                # print ('(%s %s)' % (words_all[index], words_all[index+1]))
                # print ('%s\t%s' % (words_all[index], words_all[index+1]))
                yield None, f'{words_all[index]}\t1\t{words_all[index + 1]}'
            index += 1

    def reducer_sort(self, _, values):
        for key in sorted(values, reverse=False):
            yield None, key

    def reducer_last(self, _, values):

        current_word = None
        current_count = 0
        word = None
        current_bigram = None
        index = 0
        lista = []
        lista_ost = []

        for line in values:
            # remove leading and trailing whitespace
            line = line.strip()

            # parse the input we got from mapper.py

            word, count, word2 = line.split('\t',2)
            count = int(count)
            # print(word)
            # print(word2)
            index += 1


            if current_word == word:
                current_count += count
                lista.append([current_bigram])
                current_bigram = f'({word} {word2})'

            else:
                lista.append([current_bigram])
                if current_word:
                    # write result to STDOUT
                    yield None, ('(%s *) %s' % (current_word, current_count))
                    ar = pd.DataFrame(lista)
                    procenty = ar.value_counts(normalize=True)
                    index_p = 0
                    for p in procenty:
                        zwrot = str(lista[index_p]).replace("['", "").replace("']", "")
                        if p == 1:
                            yield None, (f'{zwrot} 1')
                        else:
                            yield None, (f'{zwrot} {round(p, 3)}')
                        index_p += 1

                current_count = count
                current_word = word
                current_bigram = f'({word} {word2})'
                lista_ost = lista.copy()
                lista = []
                yield None, ('')

        if current_word == word:
            yield None, ('(%s *) %s' % (current_word, current_count))
            lista = lista_ost.copy()
            ar = pd.DataFrame(lista)
            procenty = ar.value_counts(normalize=True)
            index_p = 0
            for p in procenty:
                zwrot = str(lista[index_p]).replace("['", "").replace("']", "")
                if p == 1:
                    yield None, (f'{zwrot} 1')
                else:
                    yield None, (f'{zwrot} {round(p, 3)}')
                index_p += 1



        # yield None, values

    def steps(self):
        return [
            MRStep(mapper_init=self.mapper_init,
                   mapper=self.mapper,
                   combiner=self.combiner,
                   reducer=self.reducer_sort
                   ),
            MRStep(reducer=self.reducer_last)
        ]


if __name__ == '__main__':
   MRWordCount.run()