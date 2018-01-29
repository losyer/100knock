#coding:utf-8
import sys
from gensim.models import word2vec
import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt
from scipy.cluster.hierarchy import linkage, dendrogram


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

ward = linkage(country_vec_list, method="ward")
dendrogram(ward, leaf_font_size=1.5, orientation='left', labels=[country for country in country_name_list])
plt.title('Hierarchical Clustering Dendrogram')
plt.xlabel('distance')
plt.ylabel('country')
plt.savefig("dendrogram.pdf")