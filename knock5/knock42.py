# -*- coding: utf-8 -*-
#cabocha -f1 < neko.txt > neko.txt2.cabocha
#python knock41.py < neko.txt2.cabocha

from knock41 import F41
import sys
    
if __name__ == "__main__":
    sentenses = F41()
    for sentense in sentenses:  
        for chunk in sentense:
            for morph in chunk.morphs:
                print morph.surface.rstrip("。"),
            print "\t",
            if chunk.dst > 0:
                for morph in sentense[chunk.dst].morphs:
                    print morph.surface.rstrip("。"),
            print "\n",

"""
0, 一 	
0, 	
0, 　	猫 で ある  
1, 吾輩 は 	猫 で ある  
2, 猫 で ある  	
0, 名前 は 	無い  
1, まだ 	無い  
2, 無い  	
"""