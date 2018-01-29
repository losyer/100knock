#coding:utf-8
import plyvel,sys,json

def main(fi):
	my_db = plyvel.DB('name-artist.ldb', create_if_missing=True)
	for line in fi:
		dic = json.loads(line)
		if "name" in dic and "area" in dic:
			my_db.put(str(dic["name"]),str(dic["area"]))
	my_db.close()

if __name__ == "__main__":
	main(sys.stdin)