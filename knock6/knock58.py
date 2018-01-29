# -*- coding: utf-8 -*-
import sys
import xml.etree.ElementTree as ET
 
def main(f):
    tree = ET.parse(f)
    elem = tree.getroot()
    for dependencies in elem.findall(".//dependencies"):
        dep_tuples = []
        if dependencies.attrib.get("type") == "collapsed-dependencies":                
            for dep in dependencies.findall(".//dep"):
                dep_tuple = (
                dep.attrib.get("type"),\
                (dep[0].attrib.get("idx"),dep[0].text),\
                (dep[1].attrib.get("idx"),dep[1].text)\
                )
                dep_tuples.append(dep_tuple)
                #一文のdep_tuplesができる
        subj_hit = []
        for dep_tuple in dep_tuples:
            #nsubjを捜索
            if dep_tuple[0] == "nsubj":
                subj_hit.append(dep_tuple)
        for dep_tuple in dep_tuples:
            #dobjを探索
            if dep_tuple[0] == "dobj":
                for subj in subj_hit:
                    if dep_tuple[1][0] == subj[1][0]:
                        print "{}\t{}\t{}".format(subj[2][1],subj[1][1],dep_tuple[2][1])      
                    
if __name__ == "__main__":
    main(sys.stdin)

"""
understanding	enabling	computers
others	involve	generation
Turing	published	article
experiment	involved	translation
ELIZA	provided	interaction
"""