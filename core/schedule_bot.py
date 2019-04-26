from core.bot_handler import BotHandler
import requests


class ScheduleBot(BotHandler):
    api_key = 'd68a9179-ac0b-40a8-a3da-3f4edb10ac77'

    def get_station_schedule(self):
        request = 'https://api.rasp.yandex.net/v3.0/schedule/?apikey={}'.join(self.api_key)
        answer = requests.get(request)