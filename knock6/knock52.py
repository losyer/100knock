# -*- coding: utf-8 -*-
#python knock50.py<nlp.txt |python  knock51.py|python knock52.py
#inspired by asano

import sys
import re
from stemming.porter2 import stem

def main(f):
    for line in f:
        word = line.strip()
        print "{}\t{}".format(word, stem(word))
 
if __name__ == '__main__':
    main(sys.stdin)