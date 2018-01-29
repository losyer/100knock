from gensim.models import word2vec
import sys

# print "train model..."
# model = word2vec.Word2Vec(word2vec.LineSentence(sys.stdin), size=100, window=5, min_count=5, workers=12,sg=1,iter=1)
# # (sentences=None, size=100, alpha=0.025, window=5, min_count=5, max_vocab_size=None, sample=0.001, seed=1, workers=3, min_alpha=0.0001, sg=0, hs=0, negative=5, cbow_mean=1, hashfxn=<built-in function hash>, iter=5, null_word=0, trim_rule=None, sorted_vocab=1, batch_words=10000)
# print "done"
# print "save model..." 
# model.save('/work/sasaki.shota/knock_work/mymodel')

# python knock10/knock90.py <   4163.14s user 45.16s system 801% cpu 8:44.85 total

print "load model..."
model = word2vec.Word2Vec.load('/work/sasaki.shota/knock_work/mymodel')
print "done"

print model["United_States"]
print model.similarity('United_States', 'U.S')
nbest = model.most_similar('United_States', topn=10)
for tup in nbest:
    print '{}\t{}'.format(tup[0], tup[1])
nbest_analogy = model.most_similar(positive=['Spain','Athens'], negative=['Madrid'], topn=10)
for tup in nbest_analogy:
    print '{}\t{}'.format(tup[0], tup[1])


# [ 0.59752655  0.24365938 -0.22245471  0.0056778   0.09379213  0.44513389
#  ...
#   0.03765541 -0.22066242 -0.3046715   0.40399614]

# 0.909794810196

# U.S     0.909794867039
# US      0.82618522644
# Canada  0.782644152641
# U.S.    0.747705638409
# Hawaii  0.745170176029
# United_Kingdom  0.740532457829
# Bahamian        0.72135335207
# Canadian        0.719913542271
# Europe  0.718198895454
# Defense's       0.713509261608


# Greece  0.8211363554
# Armenia 0.753837645054
# Turkey  0.750325977802
# Egypt   0.747774899006
# Scandinavia     0.746008396149
# Russia  0.738701403141
# Denmark 0.732769548893
# Italy   0.729616522789
# Hungary 0.728189527988
# Lebanon 0.726560950279

