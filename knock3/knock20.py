# -*- coding: utf-8 -*-
import json,sys

for line in sys.stdin:
    dic = json.loads(line)
    if dic["title"] == "イギリス":
        sys.stdout.write(dic["text"])
        break