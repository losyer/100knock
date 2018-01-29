# -*- coding: utf-8 -*-
# cat hightemp.txt | cut -f1
# cat hightemp.txt | cut -f2
s1, s2 = zip(*[(line.split("\t")[0],line.split("\t")[1]) for line in open('hightemp.txt','r')])
with open("col1.txt","w") as fo1, open("col2.txt","w") as fo2:
    fo1.write("\n".join(s for s in s1))
    fo2.write("\n".join(s for s in s2))