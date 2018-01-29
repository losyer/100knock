# -*- coding: utf-8 -*-
#cabocha -f4 < neko.txt > neko.txt.cabocha
#python knock40.py < neko.txt.cabocha

import sys,re

class Morph:
    def __init__(self,surface,base,pos,pos1):
        self.surface = surface
        self.base = base
        self.pos = pos 
        self.pos1 = pos1
    
    def __str__(self):
        return "surface={},base={},pos={},pos1={}".format(self.surface,self.base,self.pos,self.pos1)
        
def PrintList(L):
    for item in L:
        print item

if __name__ == "__main__":        
    sentense_list = list()
    morph_list = list()
    for line in sys.stdin:
        if line == "\n":
            if not(len(morph_list) == 0):
                sentense_list.append(morph_list)
            morph_list = list()
        else:
            split_list = line.split("\t")
            M = Morph(split_list[1],split_list[2],split_list[3],split_list[4])
            morph_list.append(M)
        
    PrintList(sentense_list[2])

"""
surface=名前,base=名前,pos=名詞,pos1=名詞-一般
surface=は,base=は,pos=助詞,pos1=助詞-係助詞
surface=まだ,base=まだ,pos=副詞,pos1=副詞-助詞類接続
surface=無い,base=無い,pos=形容詞,pos1=形容詞-自立
surface=。,base=。,pos=記号,pos1=記号-句
"""
        