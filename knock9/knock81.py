#coding:utf8
"""
標準ライブラリが壊れて,str.replaceやreが使えなくなっちゃった人用のコード
あと、リストが大好きな人用のコード
"""
import sys
def hukugougo_load(f):
	hukugougo_list_2gram = list()
	hukugougo_list_3gram = list()
	hukugougo_list_4gram = list()
	hukugougo_list_5gram = list()
	hukugougo_list_6gram = list()

	for line in f:
		line = line.strip()
		l = len(line.split(" "))
		if l == 2:
			hukugougo_list_2gram.append(line)
		elif l == 3:
			hukugougo_list_3gram.append(line)
		elif l == 4:
			hukugougo_list_4gram.append(line)
		elif l == 5:
			hukugougo_list_5gram.append(line)
		elif l == 6:
			hukugougo_list_6gram.append(line)

	return (0,0,hukugougo_list_2gram,hukugougo_list_3gram,hukugougo_list_4gram,hukugougo_list_5gram,hukugougo_list_6gram)

def main(hukugougo_list_tup,corpus):
	for i,line in enumerate(corpus):
		tokens = line.strip().split(" ")
		for n in [2,3,4,5,6]:
			for j in xrange(len(tokens)-n):
				ngram = " ".join(token for token in tokens[j:j+n])
				if ngram in hukugougo_list_tup[n]:
					a = "_".join(token for token in tokens[j:j+n])
					tokens[j] = a
					del tokens[j+1:j+n]
		print " ".join(token for token in tokens)


if __name__ == "__main__":
	hukugougo_list_tup = hukugougo_load(sys.stdin)
	corpus = open(sys.argv[1],"r")
	main(hukugougo_list_tup,corpus)


