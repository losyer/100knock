# # -*- coding: utf-8 -*-
import cPickle as pickle
import sklearn.decomposition as decomp
from  sklearn.externals import joblib
import sys

X = pickle.load(sys.stdin)
svd = decomp.TruncatedSVD(300)
vec_d300 = svd.fit_transform(X)
joblib.dump(vec_d300,sys.argv[1])

#メモリ 約15GB
#時間　約15分
 