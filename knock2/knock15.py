# -*- coding: utf-8 -*-
#tail -n 2 hightemp.txt
N = int(raw_input('--> '))
L = [line for line in open('hightemp.txt','r')]
print "".join(line for line in L[-N:])