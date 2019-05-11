from pymongo import MongoClient
from core.schedule_bot import ScheduleBot


def create_db():
    '''This method creates and insert document with station codes'''
    client = MongoClient('localhost', 27017)
    db = client['codes']
    codes = db.codes
    if 'codes' not in client.list_database_names():
        # adding all codes of Minsk stations
        ru_codes = ScheduleBot.get_stations_codes()
        for station in ru_codes['countries'][118]['regions'][5]['settlements'][26]['stations']:
            codes.insert_one(station)
    #вынести поиск в отдельную функцию
    station = codes.find_one({'title': 'Минск, площадь Якуба Коласа'})
    print(station['codes']['yandex_code'])
