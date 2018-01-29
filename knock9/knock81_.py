#coding:utf8
import sys
#スペースが２つ続いてしまう時がある

def hukugougo_load(f):
    hukugougo_list = list()
    for line in f:
        hukugougo_list.append(line.strip())
    return hukugougo_list

def main(hukugougo_list,corpus):
    for line in corpus:
        for hukugougo in hukugougo_list:
            line = line.replace(hukugougo, hukugougo.replace(' ', '_'))
        sys.stdout.write(line)

if __name__ == "__main__":
    hukugougo_list = hukugougo_load(sys.stdin)
    corpus = open(sys.argv[1],"r")
    main(hukugougo_list,corpus)

