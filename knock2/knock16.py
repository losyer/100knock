# -*- coding: utf-8 -*-
#split -l 8 hightemp.txt
N = int(raw_input('--> '))
L = [line for line in open('hightemp.txt','r')]
sizeL = len(L)
a = sizeL % N
b = sizeL / N
nextPos = 0
for i in range(N):
	fo = open("file{}.txt".format(i+1),"w") 
	length = b+1 if i < a else b
	s = "".join(line for j,line in enumerate(L[nextPos:]) if j < length)
	nextPos += length
	print s
	fo.write(s)
	fo.close()