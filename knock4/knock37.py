# -*- coding: utf-8 -*-
import sys,knock30
from collections import defaultdict
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def main(f):
    word_dic = defaultdict(int)
    sl = knock30.parse(f)
    for s in sl:
        for word in s:
            word_dic[word["surface"]] += 1

    top_ten = []
    top_ten_labels = []
    for k, v in sorted(word_dic.items(), key=lambda x:x[1], reverse=True)[0:10]:
        top_ten.append(v)
        top_ten_labels.append(k)

    print top_ten_labels
    plt.bar(range(10), top_ten, tick_label=top_ten_labels)
    plt.savefig("output_knock37.png")
                
if __name__ == "__main__":
    main(sys.stdin)
    
"""
python knock35.py < neko.txt.mecab

彼人間中
一番獰悪
時妙
一毛
その後猫

"""