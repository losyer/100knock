# -*- coding: utf-8 -*-
#cat hightemp.txt | wc -l
print sum(1 for line in open('hightemp.txt', 'r'))