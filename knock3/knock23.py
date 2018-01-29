# -*- coding: utf-8 -*-
import re,sys

s = re.compile(r'==')
for line in sys.stdin:
    if s.match(line):
        print '{}:{}'.format(line.strip('= \n'), line.count('=')/2 - 1)
    

