# -*- coding: utf-8 -*- 
import sys,re
import xml.etree.ElementTree as ET

def MakeSentenceList(tree):
    sentence_list = list()
    elem = tree.getroot()
    for sentence in elem.findall(".//sentence"):
        word_list = list()
        for token in sentence.findall(".//token"):
            #print token[0].text
            word_list.append(token[0].text)
        if len(word_list) != 0: 
            sentence_list.append(" ".join(word for word in word_list))
    return sentence_list

def MakeReplaceSetList(tree): 
    elem = tree.getroot()
    replace_set_list = list()
    for coref in elem.findall(".//coreference/coreference"):
        ment_list = list()
        for mention in coref.findall(".//mention"):
            if mention.attrib.get("representative") == "true":
                ment_ref = mention[4].text
                #print ment_ref
            else:
                sentence_id = int(mention[0].text)
                ment = mention[4].text
                ment_tuple = (sentence_id,ment)
                ment_list.append(ment_tuple)
        else:
            replace_set = (ment_ref,ment_list)
            replace_set_list.append(replace_set)
    return replace_set_list
    
def main(sentence_list,replace_set_list):
    for i,sentence in enumerate(sentence_list):#１文もってくる
        for replace_set in replace_set_list:#replace_set もってきて
            for ment_tuple in replace_set[1]:
                if ment_tuple[0]-1 == i:
                    pattarn = re.compile(ment_tuple[1])
                    replace_string = replace_set[0] + "(" + ment_tuple[1] + ")"
                    sentence = pattarn.sub(replace_string,sentence)
        print sentence    
 
if __name__ == "__main__":
    tree = ET.parse(sys.stdin)
    sentence_list = MakeSentenceList(tree)
    replace_set_list = MakeReplaceSetList(tree)
    main(sentence_list,replace_set_list)    
"""
Natural language processing From Wikipedia , the free encyclopedia Natural language processing -LRB- NLP -RRB- is the free encyclopedia Natural language processing -LRB- NLP -RRB-(a field of computer science) , artificial intelligence , and linguistics concerned with the interactions between computers and human -LRB- natural -RRB- languages .
"""