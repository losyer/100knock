# -*- coding: utf-8 -*-
import re, sys
 
s = re.compile(r'\[\[Category:')
for line in sys.stdin:
    if s.match(line):
        print line,
