# -*- coding: utf-8 -*-
#python knock47.py < neko.txt2.cabocha

from knock41 import F41

def check_morphs(morphs,pos):
    ans = False
    for morph in morphs:
        if morph.pos == pos:
            ans  = True
            break
        else:
            pass
    return ans
    

if __name__ == "__main__":
    for i,chunks in enumerate(F41()):
        for chunk in chunks:
            output = ""
            if check_morphs(chunk.morphs,u"名詞"):
                output += chunk.chunk2str()
                check_chunk = chunk
                while check_chunk.dst != -1:
                    output += "-> " + chunks[check_chunk.dst].chunk2str()
                    check_chunk = chunks[check_chunk.dst]
                print output                                
