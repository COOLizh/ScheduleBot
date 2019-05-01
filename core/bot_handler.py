import requests
import json


class BotHandler(object):

    def __init__(self, token):
        self.token = token
        self.api_url = 'https://api.telegram.org/bot{}/'.format(token)

    def get_updates(self, offset=None, timeout=30):
        method = 'getUpdates'
        params = {'timeout': timeout, 'offset': offset}
        resp = requests.get(self.api_url + method, params)
        result_json = resp.json()['result']
        return result_json

    def send_message(self, chat_id, text, reply_markup):
        params = {'chat_id': chat_id, 'text': text, 'reply_markup': json.dumps(reply_markup)} if reply_markup else {'chat_id': chat_id, 'text': text}
        method = 'sendMessage'
        resp = requests.post(self.api_url + method, params)
        return resp

    def send_popup_message(self, callback_id, text):
        params = {'callback_query_id': callback_id, 'text': text, 'show_alert': 'True'}
        method = 'answerCallbackQuery'
        resp = requests.post(self.api_url + method, params)
        return resp

    def get_last_update(self):
        get_result = self.get_updates()
        last_update = get_result[-1] if get_result else get_result[len(get_result)]
        return last_update
