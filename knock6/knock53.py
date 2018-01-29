# -*- coding: utf-8 -*-
#inspired by hanawa
 
import sys
import xml.etree.ElementTree as ET
 
def main(f):
    tree = ET.parse(f)
    root = tree.getroot()
    for sent_elem in root[0][0]:
        for token_elem in sent_elem[0]:
            print token_elem[0].text
        print ""
 
if __name__ == "__main__":
    main(sys.stdin)