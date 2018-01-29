# -*- coding: utf-8 -*-
import sys, urllib, json, knock25
 
def main(f):
    d = dict()
    d = knock25.return_dic(f)
    filename = d['国旗画像'] #d[u'国旗画像']だとエラー
    qurl = "http://ja.wikipedia.org/w/api.php?action=query&format=json&titles=Image:" + urllib.quote(filename) + "&prop=imageinfo&iiprop=url"
    data = urllib.urlopen(qurl)
    jroot = json.loads(data.read()) 
    url = jroot["query"]["pages"]["-1"]["imageinfo"][0]["url"]
    print url
 
if __name__ == "__main__":
    main(sys.stdin)
    
"""
python knock20.py < jawiki-country.json | python knock29.py

https://upload.wikimedia.org/wikipedia/commons/a/ae/Flag_of_the_United_Kingdom.svg

"""
