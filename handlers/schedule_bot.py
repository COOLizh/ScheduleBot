from handlers.bot_handler import BotHandler
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

    def get_routes_inf(self, answer, limit, column):
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
            time = str(answer[column][index]['departure'])
            time = time[11:16]
            hour = '0' + str(now.hour) if len(str(now.hour)) == 1 else str(now.hour)
            minute = '0' + str(now.minute) if len(str(now.minute)) == 1 else str(now.minute)
            if hour > time[:2] or (hour == time[:2] and minute > time[3:5]):
                print(now.hour, now.minute, ' - ', time[:2], time[3:5])
                continue
            else:
                text += transport_types[answer[column][index]['thread']['transport_type']]
                text += '№' + answer[column][index]['thread']['number'] + ' ' + answer[column][index]['thread']['short_title']
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
        print(request)
        answer = requests.get(request)
        answer = answer.json()
        return self.get_routes_inf(answer, limit, 'schedule')

    def get_stations_schedule(self, key1, key2):
        yandex_api_url = f'https://api.rasp.yandex.net/v3.0/search/?apikey={self.yandex_api_key}&'
        station1 = 'from=' + key1 + '&'
        station2 = 'to=' + key2 + '&'
        date = 'date=' + self.get_datetime()
        request = yandex_api_url + station1 + station2 + date
        print(request)
        answer = requests.get(request)
        answer = answer.json()
        if 'error' in answer:
            return 'This route is on development ☹'
        limit = answer['pagination']['total']
        request += '&limit=' + str(limit)
        print(request)
        answer = requests.get(request)
        answer = answer.json()
        return self.get_routes_inf(answer, limit, 'segments')

    def find_stations(self, search_text):
        return mongo.find_station_code(search_text)

    @staticmethod
    def get_stations_codes():
        ru_request = F'https://api.rasp.yandex.net/v3.0/stations_list/?apikey=d68a9179-ac0b-40a8-a3da-3f4edb10ac77&lang=ru_RU&format=json'
        answer = requests.get(ru_request)
        return answer.json()
