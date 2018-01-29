#coding:utf8
import sys
import random

def main(corpus):
	for line in corpus:
		line = line.strip()
		tokens = line.split(" ")
		for i,token in enumerate(tokens):
			if token == "":
				continue
			d = random.randint(1,5)
			if i-d < 0:
				pre_c = tokens[0:i]
			else:
				pre_c = tokens[i-d:i]
			pro_c = tokens[i+1:i+1+d]
			for c in pre_c:
				if c == "":
					continue
				print "{}\t{}".format(token,c)
			for c in pro_c:
				if c == "":
					continue
				print "{}\t{}".format(token,c)

if __name__ == "__main__":
	main(sys.stdin)