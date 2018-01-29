#coding:utf-8
import plyvel,sys,json

def mk_db(fi):
	db = plyvel.DB('name-tag.ldb', create_if_missing=True)
	for line in fi:
		dic = json.loads(line)
		if "name" in dic and "tags" in dic:
			my_db.put(str(dic["name"]),json.dumps(dic["tags"]))
			#json.dumps:obj を JSON 形式の str に直列化します。
	db.close()

def search():
	db = plyvel.DB('name-tag.ldb', create_if_missing=True)

	print db.get(str("Oasis"))

	db.close()

if __name__ == "__main__":
	#mk_db(sys.stdin)
	search()