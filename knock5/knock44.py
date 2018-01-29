# -*- coding: utf-8 -*-
import pydot,sys
from knock41 import F41
 
def mkedge(chunks):
    edge = []
    for chunk in chunks:
        if chunk.dst:
            dst = chunk.dst
            dst_txt = unicode(chunks[dst].chunk2str())
            src_txt = unicode(chunk.chunk2str())
            if dst_txt != "" and src_txt != "":
                edge.append((src_txt,dst_txt))
    return edge
 
if __name__ == "__main__":
    for i,chunks in enumerate(F41()):
        if i == 7:
            edge = mkedge(chunks)
            g = pydot.graph_from_edges(edge, directed = True)
            g.write_jpeg("graph_from_edges_dot1.jpg", prog='dot')

#tupleに"edge"が入るとエラー
