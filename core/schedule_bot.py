from core.bot_handler import BotHandler
import requests


class ScheduleBot(BotHandler):
    api_key = 'd68a9179-ac0b-40a8-a3da-3f4edb10ac77'

    def get_station_schedule(self, transport_type):
        request = f'https://api.rasp.yandex.net/v3.0/schedule/?apikey={self.api_key}'
        station = '&station=s9600213'
        transport_type = '&transport_types=bus'
        request += station + transport_type
        answer = requests.get(request)
        return answer.json()

    @staticmethod
    def get_stations_codes():
        ru_request = F'https://api.rasp.yandex.net/v3.0/stations_list/?apikey=d68a9179-ac0b-40a8-a3da-3f4edb10ac77&lang=ru_RU&format=json'
        answer = requests.get(ru_request)
        return answer.json()
