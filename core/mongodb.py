'''This module organizes work with a database (add, search, etc.).
The database consists of all stations throughout Minsk '''
from pymongo import MongoClient
from handlers.schedule_bot import ScheduleBot


def create_db_codes():
    '''This function creates and insert document with station codes into the database'''
    client = MongoClient('localhost', 27017)
    database = client['codes']
    codes = database.codes
    stations_names = []

    if 'codes' not in client.list_database_names():
        # adding all codes of Minsk stations into the database
        ru_codes = ScheduleBot.get_stations_codes()

        for region in range(7):
            for settlements in ru_codes['countries'][118]['regions'][region]['settlements']:
                for station in settlements['stations']:
                    codes.insert_one(station)


def find_station_code(search_word):
    '''This function returns station code by searching text'''
    client = MongoClient('localhost', 27017)
    database = client['codes']
    codes = database.codes

    stations_names = []
    found_codes = []
    stations = codes.find({'title': {'$regex': search_word}})

    for item in stations:
        if item['title'] not in stations_names:
            found_codes.append(item['codes']['yandex_code'])
            stations_names.append(item['title'])

    # stations_names will be useful, when there will be a lot of stations, one of which will be selected by the user
    return stations_names, found_codes
