from core.bot_handler import BotHandler
import core.mongodb as mongo
import requests
import datetime


class ScheduleBot(BotHandler):
    yandex_api_key = 'd68a9179-ac0b-40a8-a3da-3f4edb10ac77'

    def get_datetime(self):
        now = datetime.datetime.now()
        month = '0' + str(now.month) if len(str(now.month)) == 1 else str(now.month)
        day = '0' + str(now.day) if len(str(now.day)) == 1 else str(now.day)
        return f'{now.year}-{month}-{day}'

    def get_routes_inf(self, answer, limit):
        # taking all needful information about routes
        transport_types = {'bus' : '🚌 ',
                          'plane': '✈️ ',
                          'train': '🚅 ',
                          'suburban': '🚆 '}
        now = datetime.datetime.now()
        routes = 'The nearest routes 📋\n'
        index = -1
        count = 0
        while count < 10:
            text = ''
            index += 1
            if index == limit:
                break
            time = str(answer['schedule'][index]['departure'])
            time = time[11:16]
            if str(now.hour) > time[:2] or (str(now.hour) <= time[:2] and str(now.minute) > time[3:5]):
                continue
            else:
                text += transport_types[answer['schedule'][index]['thread']['transport_type']]
                text += '№' + answer['schedule'][index]['thread']['number'] + ' ' + answer['schedule'][index]['thread']['short_title']
                text += ' ⌚ — ' + time + '\n'
                routes += text
                count += 1
        if routes == 'The nearest routes 📋\n':
            routes = 'Today there are no routes ☹'
        return routes

    def get_station_schedule(self, key):
        yandex_api_url = f'https://api.rasp.yandex.net/v3.0/schedule/?apikey={self.yandex_api_key}&'
        print(key)
        station = 'station=' + key + '&'
        date = 'date=' + self.get_datetime()
        request = yandex_api_url + station + date
        answer = requests.get(request)
        answer = answer.json()
        print(request)
        if 'error' in answer:
            return 'This station is on development ☹'
        limit = answer['pagination']['total']
        request += '&limit=' + str(limit)
        answer = requests.get(request)
        answer = answer.json()
        return self.get_routes_inf(answer, limit)

    def get_stations_schedule(self, key1, key2):
        yandex_api_url = f'https://api.rasp.yandex.net/v3.0/search/?apikey={self.yandex_api_key}&'
        station1 = 'from=' + key1 + '&'
        station2 = 'to=' + key2 + '&'
        date = 'date=' + self.get_datetime()
        request = yandex_api_url + station1 + station2 + date
        print(request)

    def find_stations(self, search_text):
        return mongo.find_station_code(search_text)

    @staticmethod
    def get_stations_codes():
        ru_request = F'https://api.rasp.yandex.net/v3.0/stations_list/?apikey=d68a9179-ac0b-40a8-a3da-3f4edb10ac77&lang=ru_RU&format=json'
        answer = requests.get(ru_request)
        return answer.json()
