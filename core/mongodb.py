from pymongo import MongoClient
import gridfs
import json


def create_db(ru_codes):
    '''This method creates and insert document with station codes'''
    client = MongoClient('localhost', 27017)
    db = client['codes']
    codes = gridfs.GridFS(db)
    a = codes.put(json.dumps(ru_codes), encoding='utf-8')
    print(a)
