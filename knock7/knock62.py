#coding:utf-8
import plyvel,sys,json

def main():
	name_artist_db = plyvel.DB('name-artist.ldb', create_if_missing=True)
	count = 0
	for _,value in name_artist_db:
		if value == "Japan":
			count += 1
	print count
	name_artist_db.close()

if __name__ == "__main__":
	main()