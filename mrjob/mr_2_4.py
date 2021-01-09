#https://mrjob.readthedocs.io/
from mrjob.job import MRJob
import re

from mrjob.step import MRStep
import numpy as np
WORD_RE = re.compile(r"[0-9]+")
## plus 6 zadań z dodaną wielostopniowością gdzie trzeba i z wykluczeniami: 1. największa liczba; 2 średnia arytmetyczna; 3 średnia geometryczna; 4  mediana; 5 liczba cyfr; 6 BIGRAMY
# odpalenie -> python mr_2_4.py inputTest.txt
class MRWordCount(MRJob):
    FILES = ['stop_words.txt']

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
                digit = int(word)
                yield(1, digit)
            except:
                pass

    def reducer_agg(self, key, values):
        items, mnozenie_elem = 0, 0
        lista = []
        for value in values:
            items += 1
            lista.append(value)


        yield f'mediana : {(np.median(np.array(lista)))}', (items, lista)

    def steps(self):
        return [
            MRStep(mapper_init=self.mapper_init,
                   mapper=self.mapper,
                   #combiner=self.reducer_agg,
                   reducer=self.reducer_agg),
            #MRStep(reducer=self.reducer_last)
        ]


if __name__ == '__main__':
   MRWordCount.run()