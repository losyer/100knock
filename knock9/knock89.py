import heapq
import cPickle as pickle
from tqdm import tqdm
import numpy as np
from sklearn.externals import joblib
import sys

def cos_sim(v1,v2):
    if np.linalg.norm(v1) == 0 or np.linalg.norm(v2) == 0:
        return 0.0
    else:
        v1 /= np.linalg.norm(v1)
        v2 /= np.linalg.norm(v2)
        return np.dot(v1,v2)

def nbest_analogy(vec,word2idx,base_word,sub_word,add_word,N=10):
    heap = []
    base_v, sub_v, add_v = vec[word2idx[base_word]], vec[word2idx[sub_word]] ,vec[word2idx[add_word]]
    v1 = base_v - sub_v + add_v
    for k,idx in tqdm(word2idx.items()):
        v2 = vec[idx]
        sim = cos_sim(v1,v2)
        if len(heap) < N:
            heapq.heappush(heap, (sim, k))
        else:
            heapq.heappushpop(heap, (sim, k))
    heap.sort(key=lambda x: x[0], reverse=True)
    return heap

if __name__ == '__main__':
    word_vectors = joblib.load(sys.argv[1])
    word2idx = pickle.load(open(sys.argv[2],"rb"))
    base_word, sub_word, add_word = "Spain", "Madrid", "Athens"
    heap = nbest_analogy(word_vectors,word2idx,base_word,sub_word,add_word)
    for tup in heap:
        print tup

"""
(0.90766252653627, 'Spain')
(0.88077052172502635, 'Portugal')
(0.8725621346155974, 'Sweden')
(0.86914755845619995, 'Greece')
(0.85136554561584044, 'Norway')
(0.85016321168107023, 'Denmark')
(0.83395091250616549, 'Belgium')
(0.83235100526686256, 'Italy')
(0.82900293546266013, 'Finland')
(0.82392533709499716, 'Netherlands')
"""