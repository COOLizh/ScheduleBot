from core.bot_handler import BotHandler
import core.mongodb as mongo
import requests
import datetime


class ScheduleBot(BotHandler):
    yandex_api_key = 'd68a9179-ac0b-40a8-a3da-3f4edb10ac77'
    yandex_api_url = f'https://api.rasp.yandex.net/v3.0/schedule/?apikey={yandex_api_key}&'

    def get_datetime(self):
        now = datetime.datetime.now()
        month = '0' + str(now.month) if len(str(now.month)) == 1 else str(now.month)
        day = '0' + str(now.day) if len(str(now.day)) == 1 else str(now.day)
        return f'{now.year}-{month}-{day}'

    def get_station_schedule(self, key):
        station = 'station=' + key + '&'
        date = 'date=' + self.get_datetime()
        request = self.yandex_api_url + station + date
        answer = requests.get(request)
        print(answer.json())

    def find_stations(self, search_text):
        return mongo.find_station_code(search_text)

    @staticmethod
    def get_stations_codes():
        ru_request = F'https://api.rasp.yandex.net/v3.0/stations_list/?apikey=d68a9179-ac0b-40a8-a3da-3f4edb10ac77&lang=ru_RU&format=json'
        answer = requests.get(ru_request)
        return answer.json()
