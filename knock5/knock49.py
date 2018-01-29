# -*- coding: utf-8 -*-
#python knock49.py < neko.txt2.cabocha
import itertools
from knock41 import F41

def check_morphs_pos(morphs,pos):
    ans = False
    for morph in morphs:
        if morph.pos == pos:
            ans  = True
            break
        else:
            pass
    return ans
    
def get_cmb(chunks):
    meisiku = set()
    for i,chunk in enumerate(chunks):
        if check_morphs_pos(chunk.morphs,u"名詞"):
            meisiku.add(i)
    return list(itertools.combinations(meisiku,2))
    
def noun2XorY_in_chunk(chunk,XorY):
    ans = ""
    for morph in chunk.morphs:
        if morph.pos == u"名詞":
            ans += XorY
        else:
            ans += morph.surface
    return ans
    
def cmb_sort(cmb):
    if cmb[0] < cmb[1]:
        return cmb
    else:
        return (cmb[1],cmb[0])

if __name__ == "__main__":
    for chunks in F41():
        cmbs = get_cmb(chunks)
        #名詞句の組み合わせを取得
        
        for cmb in cmbs:
            flag = False
            chain1 = list()
            chain2 = list()
            
            cmb = cmb_sort(cmb)#cmb=(i,j) i<jとなるように
            
            #iから根への係り受け関係のchainを保持するリスト作成
            check_chunk = chunks[cmb[0]]   
            while check_chunk.dst != -1:
                chain1.append(check_chunk.dst)
                if check_chunk.dst == cmb[1]:
                #根へ向う途中jが存在すればループを抜ける
                    flag = True
                    break
                check_chunk = chunks[check_chunk.dst]    
            
            #jから根へ辿りiと交わる文節kを探す        
            check_chunk = chunks[cmb[1]]          
            while check_chunk.dst != -1 and not(flag):
                chain2.append(check_chunk.dst)
                if check_chunk.dst in chain1:
                    rootk_idx = check_chunk.dst
                    break
                check_chunk = chunks[check_chunk.dst]
                
            if flag:
            #iから根に至るまでにjが存在する時の出力処理
                check_chunk = chunks[cmb[0]]
                output = noun2XorY_in_chunk(check_chunk,"X")
                while 1:
                    if check_chunk.dst == cmb[1]:
                        output += "-> " + noun2XorY_in_chunk(chunks[check_chunk.dst],"Y")
                        break
                    output += "-> " + chunks[check_chunk.dst].chunk2str()                
                    check_chunk = chunks[check_chunk.dst]
                print output
            
            else:
            #iとjがkで交わる時の出力処理
                check_chunk = chunks[cmb[0]]
                output = noun2XorY_in_chunk(check_chunk,"X")
                while 1:
                    if check_chunk.dst == rootk_idx:
                        break
                    output += "-> " + chunks[check_chunk.dst].chunk2str()
                    check_chunk = chunks[check_chunk.dst]
                
                check_chunk = chunks[cmb[1]]
                output += "|" + noun2XorY_in_chunk(check_chunk,"Y")
                while 1:
                    if check_chunk.dst == rootk_idx:
                        break
                    output += "-> " + chunks[check_chunk.dst].chunk2str()
                    check_chunk = chunks[check_chunk.dst]
                print output + "|" + chunks[rootk_idx].chunk2str()        
                
"""
Xは|Yで-> 始めて-> 人間という-> ものを|見た
Xは|Yという-> ものを|見た
Xは|Yを|見た
Xで-> 始めて-> Yという
Xで-> 始めて-> 人間という-> Yを
Xという-> Yを
"""           