#coding:utf8
import sys
import random

def main():
	pos_neg_list = list()
	fi1 = open(sys.argv[1],"r")
	for line in fi1:
		pos_neg_list.append("+1 {}".format(line.strip()))
	fi1.close()

	fi2 = open(sys.argv[2],"r")
	for line in fi2:
		pos_neg_list.append("-1 {}".format(line.strip()))
	random.shuffle(pos_neg_list)
	fi2.close()

	for sent in pos_neg_list:
		print sent

if __name__ == "__main__":
	main()

