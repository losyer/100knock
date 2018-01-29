#coding:utf-8
import sys
import cPickle as pickle
from sklearn.externals import joblib
 
search_word = "United_States"
word_vectors = joblib.load(sys.argv[1])
word2idx = pickle.load(open(sys.argv[2],"rb"))

print word_vectors[word2idx[search_word]]
