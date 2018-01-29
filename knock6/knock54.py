# -*- coding: utf-8 -*- 
import sys
import xml.etree.ElementTree as ET
 
def main(f): 
    tree = ET.parse(f)
    elem = tree.getroot()
    for token in elem.findall(".//token"):
        for word, lemma, POS in zip(token.findall(".//word"), token.findall(".//lemma"), token.findall(".//POS")):
            #.は現在のノードを選択します。これはパスの先頭に置くことで相対パスであることを示すのに役立ちます。
            #//は現在の要素配下のすべてのレベル上のすべての子要素を選択します。例えば、.//egg は木全体から egg 要素を選択します。
            #便利だなあ（今更
            print "{}\t{}\t{}".format(word.text,lemma.text,POS.text)
 
if __name__ == "__main__":
    main(sys.stdin)
"""
Natural	natural	JJ
language	language	NN
processing	processing	NN
From	from	IN
Wikipedia	Wikipedia	NNP
"""