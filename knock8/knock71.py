#coding:utf8
# import nltk
# nltk.download("stopwords")
from nltk.corpus import stopwords
stop_words = stopwords.words("english")

def check_stop_words(word):
	return word in stop_words

print check_stop_words("a")