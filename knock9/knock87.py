#coding:utf-8
import sys
import cPickle as pickle
import numpy as np
from sklearn.externals import joblib
 
search_word1 = "United_States"
search_word2 = "U.S"
word_vectors = joblib.load(sys.argv[1])
word2idx = pickle.load(open(sys.argv[2],"rb"))

vec1 = word_vectors[word2idx[search_word1]]
vec2 = word_vectors[word2idx[search_word2]]

vec1 /= np.linalg.norm(vec1)
vec2 /= np.linalg.norm(vec2)

print np.dot(vec1,vec2)

# 0.848763794118