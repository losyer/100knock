import sys

def main(f):
    for line in f:
        tokens = line.strip().split(" ")
        prepro_tokens = list()
        for token in tokens:
            if token != "":
                token = token.strip(".,!?;:()[]'\"")
                prepro_tokens.append(token)
        print " ".join(token for token in prepro_tokens if token)

if __name__ == "__main__":
    main(sys.stdin)