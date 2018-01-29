# -*- coding: utf-8 -*-
import re,sys

def remove_markup(str):
    pattern = re.compile(r"\'\'\'|\'\'")
    #r"  \'\'\'  |  \'\'  "
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

'''