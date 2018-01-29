# -*- coding: utf-8 -*-

import sys,knock30

def main(f):
    sl = knock30.parse(f)
    for dic_list in sl:
        for d in dic_list:
            if d["pos"] == "動詞":
                print d["surface"]
        

if __name__ == "__main__":
    main(sys.stdin)
    
"""
python knock31.py < neko.txt.mecab

生れ
つか
し
泣い
し
いる
始め

"""