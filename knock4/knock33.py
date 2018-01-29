# -*- coding: utf-8 -*-
import sys,knock30

def main(f):
    sl = knock30.parse(f)
    for dic_list in sl:
        for d in dic_list:
            if d["pos"] == "名詞" and d["pos1"] == "サ変接続":
                print d["surface"]
        

if __name__ == "__main__":
    main(sys.stdin)
    
"""
python knock33.py < neko.txt.mecab

見当
記憶
話
装飾
突起
運転

"""