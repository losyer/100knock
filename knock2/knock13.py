# -*- coding: utf-8 -*-
#paste col1.txt col2.txt > newtext.txt
L1 = [line.replace('\n' , '') for line in open('col1.txt','r')]
L2 = [line for line in open('col2.txt','r')]
with open('newtext.txt','w') as fo:
    fo.write(''.join(l1+'\t'+l2 for l1,l2 in zip(L1, L2)))