import sys
import re
from mrjob.job import MRJob

class MRWordCount(MRJob):

	def mapper(self, _, line):
		line = line.strip()
		line = line.lower()
		letters = re.findall(r'\w', line)
		for letter in letters:
			yield(letter, 1)

	def reducer(self, letter, counts):
		yield(letter, sum(counts))

if __name__ == '__main__':
	MRWordCount.run()