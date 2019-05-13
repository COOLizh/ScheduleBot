from pymongo import MongoClient
from core.schedule_bot import ScheduleBot


def create_db():
    '''This method creates and insert document with station codes'''
    client = MongoClient('localhost', 27017)
    db = client['codes']
    codes = db.codes
    stations_names = []
    if 'codes' not in client.list_database_names():
        # adding all codes of Minsk stations
        ru_codes = ScheduleBot.get_stations_codes()
        for station in ru_codes['countries'][118]['regions'][5]['settlements'][26]['stations']:
            codes.insert_one(station)
            stations_names.append(station['title'])
    return stations_names


def find_station_code(search_words):
    '''This method returns station code by searching text'''
    client = MongoClient('localhost', 27017)
    db = client['codes']
    codes = db.codes
    found_stations = []

    for word in search_words:
        stations = codes.find({'title': {'$regex': word}})
        found_stations.append(stations)

    for i in found_stations:
        for j in i:
            print(j)
