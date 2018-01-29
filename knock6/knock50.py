# -*- coding: utf-8 -*-
#python knock50.py < nlp.txt
import sys,re

if __name__ == "__main__":
    pattarn = re.compile(r"([A-Z]).*?(\.|\;|\:|\?|\!)")
    for segment in sys.stdin:
        for sentense in pattarn.finditer(segment):
            print sentense.group()