from pymongo import MongoClient
import gridfs


def create_db(ru_codes):
    '''This method creates and insert document with station codes'''
    client = MongoClient('localhost', 27017)
    db = client['codes']
    codes = db.codes
    codes.insert_one(ru_codes)
    print(db.insert_one(ru_codes).inserted_id)
