# -*- coding: utf-8 -*-
# cat hightemp.txt | cut -f1 | sort | uniq
for s in set([line.split('\t')[0] for line in open('hightemp.txt','r')]):
    print s