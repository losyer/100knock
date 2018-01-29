# -*- coding: utf-8 -*-
import re,sys

def remove_markup(str):
    pattern = re.compile(r"\[\[|\]\]|<.+?>|\{\{|\}\}|\'\'\'|\'\'|\[.+?\]")
    return pattern.sub(r"", str)

def main(f):
    d = dict()
    s = re.compile(r"\|(.+?) = (.+)")
    for line in f:
        if line.startswith('{{基礎情報'):
            for line in f:
                for kiso in s.finditer(line):
                    d[kiso.group(1)] = remove_markup( kiso.group(2) )
                if line.startswith( "}}\n" ):
                    break
            break
        
    for field, value in d.iteritems():
        print '{} = {}' .format(field, value)


if __name__ == "__main__" :
    main(sys.stdin)
                
'''
python knock20.py < jawiki-country.json | python knock26.py 

GDP統計年元 = 2012
ISO 3166-1 = GB / GBR
通貨 = スターリング・ポンド|UKポンド (&pound;)
国際電話番号 = 44
公用語 = 英語（事実上）
人口順位 = 22
人口密度値 = 246
日本語国名 = グレートブリテン及び北アイルランド連合王国
標語 = lang|fr|Dieu et mon droit（フランス語:神と私の権利）
確立年月日2 = 1707年
確立年月日3 = 1801年
確立年月日1 = 927年／843年

'''