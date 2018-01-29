# -*- coding: utf-8 -*-
import re,sys

def return_dic(f):
    d = dict()
    s = re.compile(r"\|(.+?) = (.+)")
    for line in f:
        if line.startswith('{{基礎情報'):
            for line in f:
                for kiso in s.finditer(line):
                    d[kiso.group(1)] = kiso.group(2)
                if line.startswith( "}}\n" ):
                    break
            break
    return d

if __name__ == "__main__" :
    d= dict()
    d = return_dic(sys.stdin)          
    for field, value in d.iteritems():
        print '{} = {}' .format(field, value)
                
'''
python knock20.py < jawiki-country.json | python knock25.py 

GDP統計年元 = 2012
ISO 3166-1 = GB / GBR
通貨 = [[スターリング・ポンド|UKポンド]] (&pound;)
国際電話番号 = 44
公用語 = [[英語]]（事実上）
人口順位 = 22
人口密度値 = 246
...

'''