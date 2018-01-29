#coding:utf-8
import sys
from gensim.models import word2vec
import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt
from scipy.cluster.hierarchy import linkage, dendrogram
from sklearn.manifold import TSNE

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

tsne = TSNE(n_components=2)
 
country_vec_tsne = tsne.fit_transform(country_vec_list)
plt.scatter(country_vec_tsne[:, 0], country_vec_tsne[:, 1], s=0.01)
plt.title('t-SNE')
plt.xlabel('x')
plt.ylabel('y')
for country_name, vec in zip(country_name_list, country_vec_tsne):
    plt.annotate(country_name, xy = (vec[0], vec[1]), size = 3.)
plt.savefig("tsne.pdf")