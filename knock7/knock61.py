#coding:utf-8
import plyvel,sys,json

def main():
	name_artist_db = plyvel.DB('name-artist.ldb', create_if_missing=True)
	print name_artist_db.get(str("特定の（指定された）アーティスト"))
	name_artist_db.close()

if __name__ == "__main__":
	main()