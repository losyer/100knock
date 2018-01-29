# -*- coding: utf-8 -*-
import sys
import xml.etree.ElementTree as ET
 
def main(f): 
    tree = ET.parse(f)
    elem = tree.getroot()
    for token in elem.findall(".//token"):
        for word,ner in zip(token.findall(".//word"),token.findall(".//NER")):
            if ner.text == "PERSON":
                print "{}".format(word.text)
 
if __name__ == "__main__":
    main(sys.stdin)
    
"""
Alan
Turing
Joseph
Weizenbaum
MARGIE
Schank
Wilensky
Meehan
Lehnert
Carbonell
Lehnert
Jabberwacky
Moore
"""