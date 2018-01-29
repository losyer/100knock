# -*- coding: utf-8 -*-
# cat hightemp.txt | tr '\t' ' ' > hightemp_2.txt
for line in open('hightemp.txt', 'r'):
    print line.expandtabs(1),