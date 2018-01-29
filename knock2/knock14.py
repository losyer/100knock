# -*- coding: utf-8 -*-
#head -n 2 hightemp.txt
import sys
N = sys.argv[1]
print "".join(line for i,line in enumerate(open('hightemp.txt','r')) if i <= int(N)-1)