# -*- coding: utf-8 -*-
import sys,knock30

def main(f):
    sl = knock30.parse(f)
    flag_of_noun = False
    flag_of_noun2 = False
    meisi = ""
    for dic_list in sl:
        for d in dic_list:     
            if flag_of_noun2 and d["pos"] != "名詞":
                print meisi
                meisi = ""
                flag_of_noun = False
                flag_of_noun2 = False
            elif flag_of_noun and d["pos"] != "名詞":
                flag_of_noun = False
                meisi = ""
            elif flag_of_noun and d["pos"] == "名詞":
                flag_of_noun2 = True
                meisi += d["surface"]
            elif not(flag_of_noun) and d["pos"] == "名詞":
                flag_of_noun = True
                meisi += d["surface"]
                
if __name__ == "__main__":
    main(sys.stdin)
    
"""
python knock35.py < neko.txt.mecab

彼人間中
一番獰悪
時妙
一毛
その後猫

"""