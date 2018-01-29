#coding:utf8
import sys
from collections import defaultdict
import json
from tqdm import tqdm
import cPickle
from sklearn.externals import joblib

def main(t_c_pairs_file):
	count = 0
	cooccur_dic = defaultdict(int)
	t_dic = defaultdict(int)
	c_dic = defaultdict(int)
	print "start cal freq"
	for line in tqdm(t_c_pairs_file, total=689596588):
		line = line.strip()
		cols = line.split("\t")
		if len(cols) != 2:

			count += 1
			continue
		t,c = cols[0],cols[1]
		cooccur_dic[(t,c)] += 1
		t_dic[t] += 1
		c_dic[c] += 1
	print "len(cols) != 2 count = {}".format(count)
	return cooccur_dic,t_dic,c_dic

def make_text_dictionary(cooccur_dic,t_dic,c_dic):
	fo1 = open(sys.argv[1],"w")
	fo2 = open(sys.argv[2],"w")
	fo3 = open(sys.argv[3],"w")
	for k,v in tqdm(sorted(cooccur_dic.items(),key=lambda x:x[1],reverse=True)):
		fo1.write("{}\t{}\t{}\n".format(k[0],k[1],v))

	for k,v in tqdm(sorted(t_dic.items(),key=lambda x:x[1],reverse=True)):
		fo2.write("{}\t{}\n".format(k,v))

	for k,v in tqdm(sorted(c_dic.items(),key=lambda x:x[1],reverse=True)):
		fo3.write("{}\t{}\n".format(k,v))
	fo1.close()
	fo2.close()
	fo3.close()

if __name__ == "__main__":
	print "make 3 dics"
	cooccur_dic,t_dic,c_dic = main(sys.stdin)

	print "make text dic"
	make_text_dictionary(cooccur_dic,t_dic,c_dic)
	print "done"

