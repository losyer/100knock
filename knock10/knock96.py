#coding:utf-8
import sys
from sklearn.externals import joblib
from gensim.models import word2vec

model = word2vec.Word2Vec.load('/work/sasaki.shota/knock_work/mymodel')
for line in sys.stdin:
    try:
        model[line.strip()]#取り出した
    except:
        pass