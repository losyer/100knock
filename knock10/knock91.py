import sys

flag = 0
for line in sys.stdin:
    if line.startswith(": family"):
        flag = 1
        continue
    if line.startswith(": ") and flag == 1:
        break
    if flag == 1:
        print line,