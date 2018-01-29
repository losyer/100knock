# -*- coding: utf-8 -*-
#python knock46.py < neko.txt2.cabocha

from knock41 import F41
from collections import OrderedDict

if __name__ == "__main__":
    for chunks in F41():
        for chunk in chunks:
            for morph in chunk.morphs:
                if morph.pos == u"動詞":
                    dousi = morph.base
                    zyosi_list = list()
                    kou_list = list()
                    for src in chunk.srcs:
                        zyosi = ""
                        for morph2 in chunks[src].morphs:
                            if morph2.pos == u"助詞":
                                zyosi = morph2.base
                                kou ="".join(morph2.surface for morph2 in chunks[src].morphs)
                        if zyosi != "":
                            zyosi_list.append(zyosi)
                            kou_list.append(kou)                            
                    zyosi_kou_dic = dict(zip(zyosi_list,kou_list))
                    #sortした後、辞書の形を保持するOrderedDict
                    dic = OrderedDict(sorted(zyosi_kou_dic.items()))
                    zyosi = " ".join(dic.keys())
                    kou = " ".join(dic.values())                        
                    if len(zyosi) != 0:
                        print "{}\t{} {}".format(dousi,zyosi,kou)
                    #最左の動詞という条件があるので
                    #これ以上動詞を探すのをやめる
                    break

