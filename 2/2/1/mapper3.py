#!/usr/bin/env python3
"""mapper3.py"""

import sys
import re

# input comes from STDIN (standard input)
for line in sys.stdin:
    line = line.strip()
    line = line.lower()
    numbers = re.findall(r'\d+', line)

    for number in numbers:
        print ('%s\t%s' % (number, 1))
#
#/usr/local/hadoop/bin/hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.8.2.jar -file /home/student/mapper3.py -mapper /home/student/mapper3.py -file /home/student/reducer3.py -reducer /home/student/reducer3.py -input tutorial/books -output tutorial/books-streaming-out-pyt3		

