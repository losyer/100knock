# -*- coding: utf-8 -*-
#cut -f1 hightemp.txt | sort | uniq -c | sort -r
from collections import defaultdict
dic = defaultdict(int)
for line in open('hightemp.txt','r'):
    dic[line.split('\t')[0]] += 1
for s, freq in sorted(dic.iteritems(),key=lambda x:x[1]):
    print "{}\t{}".format(s, freq)