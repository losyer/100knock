# -*- coding: utf-8 -*-
#sort -nk3,3  hightemp.txt
Row = [line.split("\t") for line in open('hightemp.txt','r')]
for r in sorted(Row, key=lambda x:x[2],reverse=True):
    print "\t".join(elem for elem in r),