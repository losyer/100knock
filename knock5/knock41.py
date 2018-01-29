# -*- coding: utf-8 -*-
#cabocha -f1 < neko.txt > neko.txt2.cabocha
#python knock41.py < neko.txt2.cabocha

from knock40 import Morph
import sys

class Chunk:
    def __init__(self,morphs,dst,srcs):
        self.morphs = morphs
        self.dst = dst
        self.srcs = srcs
        
    def __str__(self):
        return "morphs={},dst={},srcs={}".format(self.morphs,self.dst,self.srcs)
    
    def chunk2str(self):
        output = []
        for morph in self.morphs:
            if morph.pos == u"記号":
                pass
            else:
                output.append(morph.surface)
        return "".join(output)
        
def GetSrcs(chunks,chunk_index):
    srcs = list()
    for i,chunk in enumerate(chunks):
        if chunk_index == chunk.dst:
            srcs.append(i)
    return srcs
    
def F41():
    sentenses= list()
    morphs = list()
    chunks = list()
    for line in sys.stdin:
        if line.startswith("*"):
            # *が来たのを合図に前のmorphsをchunkとして格納
            #初めの*だけ例外
            if not(len(morphs) == 0):          
                c = Chunk(morphs,dst,srcs)
                chunks.append(c)
                morphs = list()
            sp_line = line.split(" ")
            chunk_index = int(sp_line[1])
            dst = int(sp_line[2].rstrip("D"))
            srcs = GetSrcs(chunks,chunk_index)
            
        elif line.startswith("EOS"):
            #EOSでも同様に前のmorphsをchunkとして格納
            #その後chunksをsenteseとして格納
            c = Chunk(morphs,dst,srcs)
            chunks.append(c)
            morphs = list()
            sentenses.append(chunks)
            chunks = list()
        else:
            sp_line2 = line.split("\t")
            sp_line3 = sp_line2[1].split(",")
            surface = unicode(sp_line2[0])
            pos = sp_line3[0]
            pos1 = sp_line3[1]
            base = sp_line3[6]
            m = Morph(surface,base,pos,pos1)
            morphs.append(m)
    return(sentenses)
    
if __name__ == "__main__":                    
    sentenses = F41()
    for i,chunk in enumerate(sentenses[7]):
        print "{},".format(i),
        for morph in chunk.morphs:
            print morph.surface,
        print "\t係り先:{}".format(chunk.dst)
        
"""
0, 吾輩 は     係り先:5
1, ここ で     係り先:2
2, 始め て     係り先:3
3, 人間 という 係り先:4
4, もの を     係り先:5
5, 見 た 。    係り先:-1
"""
