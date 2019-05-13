from core.bot_handler import BotHandler
import core.mongodb as mongo
import requests


class ScheduleBot(BotHandler):
    api_key = 'd68a9179-ac0b-40a8-a3da-3f4edb10ac77'

    def parse_text(self, text: str):
        '''This function breaks the string into separate words'''
        punctuation_marks = (',', '.', '!', '?', '-')
        for mark in punctuation_marks:
            text = text.replace(mark, ' ')
        return text.split()

    def get_station_schedule(self, search_text):
        words = self.parse_text(search_text)
        mongo.find_station_code(words)
        #request = f'https://api.rasp.yandex.net/v3.0/schedule/?apikey={self.api_key}'
        #answer = requests.get(request)
        #return answer.json()

    @staticmethod
    def get_stations_codes():
        ru_request = F'https://api.rasp.yandex.net/v3.0/stations_list/?apikey=d68a9179-ac0b-40a8-a3da-3f4edb10ac77&lang=ru_RU&format=json'
        answer = requests.get(ru_request)
        return answer.json()
