#coding:utf-8
import sys
from scipy.stats import spearmanr

sim_list1, sim_list2 = [],[]
for line in sys.stdin:
    line = line.strip()
    col = line.split("\t")
    sim_list1.append(float(col[2]))
    sim_list2.append(float(col[3]))

print spearmanr(sim_list1,sim_list2)
"""
Word2Vec
SpearmanrResult(correlation=0.64450168564407184, pvalue=8.0177288738837747e-43)

SVD_vec
SpearmanrResult(correlation=0.52140242950410975, pvalue=5.3361778816017704e-26) 
"""