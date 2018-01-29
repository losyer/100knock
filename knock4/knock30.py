# -*- coding: utf-8 -*-
import sys

def output(sentense_list):
    for sl in sentense_list[0:3]:
        for s in sl:
            for k, v in s.items():
                print k, v
        print ""

def parse(f):
    sentense_list = list()
    dict_list = list()
    for line in f:
        if line != "EOS\n":
            l1 = line.split("\t")
            l2 = l1[1].split(",")
            d = dict()
            d["surface"] = l1[0]
            d["pos"] = l2[0]
            d["pos1"] = l2[1]
            d["base"] = l2[6]
            dict_list.append(d)
        if line == "EOS\n":
            sentense_list.append(dict_list)
            dict_list = list()
    return sentense_list
                 
if __name__ == "__main__":
    sentense_list = parse(sys.stdin)
    output(sentense_list)
    
"""
python knock30.py < neko.txt.mecab

"""
