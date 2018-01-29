# -*- coding: utf-8 -*-
import re,sys

def main(f):
    s = re.compile(r'\[\[(File:.+?)\|')
    for line in f:
        search = s.search(line)
        if search :
            print search.group(1)
        
if __name__ == "__main__":
    main(sys.stdin)
    
'''
python knock20.py < jawiki-country.json | python knock24.py 

File:Battle of Waterloo 1815.PNG
File:The British Empire.png
...
File:Heathrow T5.jpg
File:Anglospeak.svg
'''