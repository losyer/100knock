# -*- coding: utf-8 -*-
#cabocha -f1 < neko.txt > neko.txt2.cabocha
#python knock43.py < neko.txt2.cabocha

from knock41 import F41
import sys
    
if __name__ == "__main__":
    sentenses = F41()
    
    for sentense in sentenses:  
        for chunk in sentense:
            chunkstr = ""
            nounflag = False
            verbflag = False
            for morph in chunk.morphs:
                if morph.pos == u"名詞":
                    nounflag = True
                    a = morph.surface
                chunkstr += morph.surface.rstrip("。|、")
            chunkstr += "\t"
            if chunk.dst > 0 and nounflag:
                for morph in sentense[chunk.dst].morphs:
                    if morph.pos == u"動詞":
                        verbflag = True
                        b = morph.surface  
                    chunkstr += morph.surface.rstrip("。|、")
                if verbflag:
                    #print "名詞＝{}".format(a)
                    #print "動詞＝{}".format(b)
                    print chunkstr 
                
"""
　どこで	生れたか
見当が	つかぬ
所で	泣いて
ニャーニャー	泣いて
いた事だけは	記憶している
"""