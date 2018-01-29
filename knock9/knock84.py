#coding:utf8
import sys
import json
from scipy.sparse import lil_matrix
import numpy as np
from math import log
from tqdm import tqdm	
import cPickle
from sklearn.externals import joblib

N = 688515970#(strip4)

def text_dic_load(path1,path2,path3):
	f1 = open(path1,"r")
	f2 = open(path2,"r")
	f3 = open(path3,"r")
	cooccur_dic = dict()
	t_dic = dict()
	c_dic = dict()
	for line in tqdm(f1,total=129679367):
		col = line.strip().split("\t")
		cooccur_dic[(col[0],col[1])] = int(col[2])
	for line in f2:
		col = line.strip().split("\t")
		t_dic[col[0]] = int(col[1])
	for line in f3:
		col = line.strip().split("\t")
		c_dic[col[0]] = int(col[1])
	f1.close()
	f2.close()
	f3.close()
	return cooccur_dic,t_dic,c_dic

def make_word2index(t_dic,c_dic):
	word2index = dict()
	for k,v in t_dic.iteritems():
		word2index.setdefault(k,len(word2index))
	for k,v in c_dic.iteritems():
		word2index.setdefault(k,len(word2index))
	return word2index

def cal_ppmi(t_c,t,c):
	if t_c < 10:
		return 0
	else:
		result = log(t_c*N / float(t) / float(c))
		if result < 0:
			return 0
		else:
			return result	

def main(cooccur_dic,t_dic,c_dic,word2index):
	size = len(word2index)
	X = lil_matrix((size,size),dtype=np.float)
	for k,v in tqdm(cooccur_dic.iteritems(),total=129680307):
		t,c = k[0],k[1]
		t_idx,c_idx = word2index[t],word2index[c]
		ppmi = cal_ppmi(v,t_dic[t],c_dic[c])
		if ppmi != 0:
			X[t_idx,c_idx] = float(ppmi)
	return X

if __name__ == "__main__":
	print "file open , text dictionary load"
	cooccur_dic,t_dic,c_dic = text_dic_load(sys.argv[1],sys.argv[2],sys.argv[3])

	print "make word2index"
	word2index = make_word2index(t_dic,c_dic)
	print "len word2index = {}".format(len(word2index))

	print "pkl dump word2idx"
	cPickle.dump(word2index,open(sys.argv[4], 'w'))

	print "cal ppmi(about 10min)"
	X = main(cooccur_dic,t_dic,c_dic,word2index)

	print "pkl dump X"
	fo = open(sys.argv[5],"wb")
	cPickle.dump(X,fo)
	fo.close()
	print "done"
