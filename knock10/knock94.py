#coding:utf-8
import sys
import argparse
from sklearn.externals import joblib
import cPickle as pickle
import numpy as np

def use_word2vec():
    from gensim.models import word2vec
    model = word2vec.Word2Vec.load('/work/sasaki.shota/knock_work/mymodel')

    for i,line in enumerate(sys.stdin):
        if i == 0:
            continue
        line = line.strip()
        col = line.split("\t")
        line = line + "\t{}".format(model.similarity(col[0], col[1]))
        print line

def cos_sim(vec1,vec2):
    norm1 = np.linalg.norm(vec1)
    norm2 = np.linalg.norm(vec2)
    if norm1 !=0 and norm2 != 0:
        vec1 /= norm1
        vec2 /= norm2
        return np.dot(vec1,vec2)
    else:
        return 0

def use_SVDvec(args):
    svd_vectors = joblib.load(args.svdvec)
    word2idx = pickle.load(open(args.svdw2idx,"rb"))
    for i,line in enumerate(sys.stdin):
        if i == 0:
            continue
        line = line.strip()
        col = line.split("\t")
        alt1_vec, alt2_vec = svd_vectors[word2idx[col[0]]], svd_vectors[word2idx[col[1]]]
        line = line + "\t{}".format(cos_sim(alt1_vec,alt2_vec))
        print line

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-w2v',action='store_true'
        )
    parser.add_argument(
        '-SVD', action='store_true'
        )
    parser.add_argument(
        "-svdvec", type=str
        )
    parser.add_argument(
        "-svdw2idx", type=str
        )
    args = parser.parse_args()

    if args.w2v:
        use_word2vec()
    elif args.SVD:
        use_SVDvec(args)



"""
word2vec

love    sex     6.77    0.593031694696
tiger   cat     7.35    0.833956152982
tiger   tiger   10.00   1.0
book    paper   7.46    0.676500441959

SVD_vec
love    sex     6.77    0.357930273952
tiger   cat     7.35    0.456267047542
tiger   tiger   10.00   1.0
book    paper   7.46    0.542431122294
"""
