# -*- coding: utf-8 -*-
#python knock47.py < neko.txt2.cabocha

from knock41 import F41
from collections import OrderedDict

if __name__ == "__main__":
    for i,chunks in enumerate(F41()):
        for chunk in chunks:
            meisi_flag = False
            for morph in chunk.morphs:
                if meisi_flag:
                    if morph.surface != u"を":
                        meisi_flag = False
                    else:
                        zyosi_list = list()
                        kou_list = list()
                        if chunks[chunk.dst].morphs[0].pos == u"動詞":
                            dousi = chunks[chunk.dst].morphs[0].base                            
                            for src in chunks[chunk.dst].srcs:
                                kou = ""
                                zyosi = ""
                                for morph2 in chunks[src].morphs:
                                    if morph2.pos == u"助詞":
                                        zyosi = morph2.base
                                        kou =  chunks[src].chunk2str()
                                if len(zyosi) != "":
                                    zyosi_list.append(zyosi)
                                    kou_list.append(kou)
                            zyosi_kou_dic = dict(zip(zyosi_list,kou_list))
                            #sortした後、辞書の形を保持するOrderedDict
                            dic = OrderedDict(sorted(zyosi_kou_dic.items()))
                            zyosi = " ".join(dic.keys())
                            kou = " ".join(dic.values())                        
                            if len(zyosi) != 0:
                                print "{}を{}\t{}\t{}".format(meisi,dousi,zyosi,kou)
                                            
                if morph.pos == u"名詞" and morph.pos1 == u"サ変接続":
                    meisi = morph.base
                    meisi_flag = True
#「〜を」が入ってくる状態