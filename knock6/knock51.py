# -*- coding: utf-8 -*-
#python knock50.py < nlp.txt | python knock51.py
import sys,re

if __name__ == "__main__":
    for sentense in sys.stdin:
        print sentense.replace(" ","\n")
