# -*- coding: utf-8 -*-
ngram = lambda x,n :{x[i:i+n] for i in range(len(x)-n+1)}
X = ngram("paraparaparadise",2)
Y = ngram("paragraph",2)
# print "X = {}\nY = {}\nX|Y = {}\nX&Y = {}\nX-Y = {}\n'se' in X = {}\n'se' in Y = {}".format(X,Y,X|Y,X&Y,X-Y,"se"in X,"se"in Y)
print("X = {}\nY = {}\nX|Y = {}\nX&Y = {}\nX-Y = {}\n'se' in X = {}\n'se' in Y = {}".format(X,Y,X|Y,X&Y,X-Y,"se"in X,"se"in Y))