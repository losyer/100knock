cat baseline.txt | classias-tag -m baseline.model -p -r | sed s/"\s"/"\t"/g | sed s/":"/"\t"/g