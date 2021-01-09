#https://mrjob.readthedocs.io/
from mrjob.job import MRJob
import re

from mrjob.step import MRStep

WORD_RE = re.compile(r"[0-9]+")
suma = 0

class MRWordCount(MRJob):

   suma = 0
   ile = 1
   def mapper(self, _, line):
      #for word in WORD_RE.findall(line):
      #   word = word.lower()
      #   yield word
      for word in WORD_RE.findall(line):
         try:
            digit = int(word)
            yield(digit, 1)
         except:
            pass

   def reducer(self, word, counts):
      self.suma += word
      self.ile += 1
      wynik = self.suma/self.ile
      yield  wynik, (word, sum(counts))

   # def reducer_find(self, _, word_count_pairs):
   #    # each item of word_count_pairs is (count, word),
   #    # so yielding the top 15 results in key=counts, value=word
   #    # for val in nlargest(20, word_count_pairs):
   #    #    yield val
   #    yield (word_count_pairs, self.suma/self.ile)

   # def steps(self):
   #    return [
   #       MRStep(mapper=self.mapper,
   #              reducer=self.reducer),
   #       MRStep(reducer=self.reducer_find)
   #    ]

if __name__ == '__main__':
   MRWordCount.run()