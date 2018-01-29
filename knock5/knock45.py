# -*- coding: utf-8 -*-
#python knock45.py < neko.txt2.cabocha> output.txt

from knock41 import F41

if __name__ == "__main__":
    for chunks in F41():
        for chunk in chunks:
            for morph in chunk.morphs:
                if morph.pos == u"動詞":
                    dousi = morph.base
                    zyosi_list = list()
                    for src in chunk.srcs:
                        zyosi = ""
                        for morph in chunks[src].morphs:
                            if morph.pos == u"助詞":
                                zyosi = morph.base
                        if zyosi != "":
                            zyosi_list.append(zyosi)
                    zyosi_list.sort()
                    #"が"のほうが"と"より先に来る
                    zyosi = " ".join(zyosi_list)
                    if len(zyosi) != 0:
                        print "{}\t{}".format(dousi,zyosi)
                    #最左の動詞という条件があるので
                    #これ以上動詞を探すのをやめる
                    break
"""                    
cat output.txt | sort | uniq -c | sort -nr | head -20
704 云う	と
452 する	を
333 思う	と
    
cat result45.txt | sort | uniq -c | sort -rn | grep -w する |head -20
.
.
.
"""
