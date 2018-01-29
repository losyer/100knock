#coding:utf-8
import sys
from sklearn.externals import joblib
from gensim.models import word2vec
from sklearn.cluster import KMeans

print "model load"
model = word2vec.Word2Vec.load('/work/sasaki.shota/knock_work/mymodel')
country_vec_list, country_name_list = list(), list()
for line in sys.stdin:
    country_name = line.strip()
    try:
        country_vec_list.append(model[country_name])
        country_name_list.append(country_name)
    except:
        continue

# country_names = country_vec_dic.keys()
# country_vec_list = country_vec_dic.values()

km = KMeans(n_clusters=5)
country_vec_km = km.fit(country_vec_list)
labels = country_vec_km.labels_
for country_name, label in zip(country_name_list, labels):
    print country_name, label
