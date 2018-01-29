# -*- coding: utf-8 -*-
#d["pos1"]="連体化"を使わないでやる
import sys,knock30

def main(f):
    sl = knock30.parse(f)
    flag_of_noun = False
    flag2 = False
    for dic_list in sl:
        for d in dic_list:     
            if flag2 and d["pos"] == "名詞":
                print meisiku + d["surface"]
                frag_of_noun = False
                flag2 = False
            elif flag2 and d["pos"] != "名詞":
                flag_of_noun = False
                flag2 = False
            elif flag_of_noun and d["surface"] == "の":
                flag2 = True
                meisiku += "の"
            elif flag_of_noun and d["surface"] != "の":
                flag_of_noun = False    
            elif d["pos"] == "名詞":
                flag_of_noun = True
                meisiku = d["surface"]
                
if __name__ == "__main__":
    main(sys.stdin)
    
"""
python knock33.py < neko.txt.mecab

彼の掌
掌の上
書生の顔
はずの顔
顔の真中
穴の中

"""