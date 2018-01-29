# -*- coding: utf-8 -*-
#Copyright (c) 2016 reina.a All Rights Resereved
import sys
from lxml import etree
from nltk.tree import Tree
 
def main(fi):
    root = etree.parse(fi)#xmlを解析
    parses = root.xpath('//parse')#S式解析結果の部分を取り出す
    for parse in parses:#parseは１文の解析element
        tree = Tree.fromstring(parse.text)#句構造のテキストを木の形に
        for s in tree.subtrees():
            #subtreeを全て列挙して一つずつ見ていく
            #木を根（親）からはがしていくような感じ？
            if s.label() == 'NP':
                print ' '.join(s.leaves())#ラベルにNPを見つけたら葉を出力
               
if __name__ == "__main__":
    main(sys.stdin)

"""
↓print tree
(ROOT
  (S
    (PP
      (NP (JJ Natural) (NN language) (NN processing))
      (IN From)
      (NP (NNP Wikipedia)))
    (, ,)
    (NP
      (NP
        (DT the)
        (JJ free)
        (NN encyclopedia)
        (JJ Natural)
        (NN language)
        (NN processing))
      (PRN (-LRB- -LRB-) (NP (NN NLP)) (-RRB- -RRB-)))
    (VP
      (VBZ is)
      (NP
        (NP
          (NP (DT a) (NN field))...

"""