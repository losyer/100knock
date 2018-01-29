#coding:utf8
from stemming.porter2 import stem
from nltk.corpus import stopwords
import sys
stop_words = stopwords.words("english")

def check_stop_words(word):
	return word in stop_words

def baseline(line, stop_list):
    word_ls = line.split()
    # ストップワード除去
    for word in word_ls:
        if check_stop_words(word):
            word_ls = filter(lambda a: a != word, word_ls)
    # ステミング
    for i in range(len(word_ls)):
        word_ls[i] = stem(word_ls[i].strip())
    return word_ls

if __name__ == "__main__":
    text = sys.stdin
    for line in text:
		print " ".join(baseline(line, stop_words))