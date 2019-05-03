from pymongo import MongoClient


def create_db(ru_codes):
    '''This method creates and insert document with station codes'''
    client = MongoClient('localhost', 27017)
    db = client.codes
    db.insert_one(ru_codes)
    print(db.find_one())