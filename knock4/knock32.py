# -*- coding: utf-8 -*-
import sys,knock30

def main(f):
    sl = knock30.parse(f)
    for dic_list in sl:
        for d in dic_list:
            if d["pos"] == "動詞":
                print d["base"]
        

if __name__ == "__main__":
    main(sys.stdin)
    
"""
python knock32.py < neko.txt.mecab

生れる
つく
する
泣く
する
いる
始める

"""