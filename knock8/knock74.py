#coding:utf8
import sys
from math import exp
from stemming.porter2 import stem


def prepro(text):
    word_ls = text.split()
    # ステミング
    for i in range(len(word_ls)):
        word_ls[i] = stem(word_ls[i].strip())
    return " ".join(word_ls)

def classify(text, model):
    text_word = text.split()
    weight = 0.0
    for line in model:
        weight_word = line.split()
        if weight_word[0] == "@classias":
            continue
        elif weight_word[1] == "__BIAS__":
            bias = float(weight_word[0])
        else:
            if weight_word[1] in text_word:
                weight += float(weight_word[0])
    weight_bias = weight + bias
    prob = 1/(1 + exp(weight_bias))
    if weight_bias > 0:
        return "{}\t{}".format("+1", prob)
    else:
        return "{}\t{}".format("-1", prob)

if __name__ == "__main__":
    text = "the movie is beautiful amazing good happy"
    print prepro(text)
    print classify(prepro(text),sys.stdin)