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

def nbest(vec,word2idx,word,N=10):
    heap = []
    v1 = vec[word2idx[word]]
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
    heap = nbest(word_vectors,word2idx,"England")
    for tup in heap:
        print tup

"""
(1.0, 'England')
(0.78692840818248544, 'Scotland')
(0.7171003176862274, 'Wales')
(0.66189611464286147, 'Ireland')
(0.62786302728205556, 'Australia')
(0.6240576862964845, "Yard's")
(0.6060247433799173, 'Somerset')
(0.59883947685820826, 'Yorkshire')
(0.59078021001795444, 'Britain')
(0.56225155806189142, 'New_Zealand')
"""