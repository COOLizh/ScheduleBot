import datetime
import core.mongodb as mongo
from core.schedule_bot import ScheduleBot
from core.keyboards import *


def main():
    token = '826030216:AAEOSvYrw1V5-q4vBbS-h8l81s-jEwz52AE'
    schedule_bot = ScheduleBot(token)
    mongo.create_db_codes()
    now = datetime.datetime.now()
    new_offset = None
    today = now.day
    hour = now.hour

    while True:
        schedule_bot.get_updates(new_offset)
        last_update = schedule_bot.get_last_update()
        last_update_id = last_update['update_id']

        last_sent_text = last_update['message']['text']
        last_chat_id = last_update['message']['chat']['id']
        if last_sent_text:
            schedule_bot.send_message(last_chat_id, 'Enter the name of station.', False)
            schedule_bot.get_station_schedule(last_sent_text)

        '''
        if 'message' in last_update.keys():
            last_chat_id = last_update['message']['chat']['id']
            if last_update['message']['text'] == '/start':
                reply_markup = get_transport_keyboard()
                schedule_bot.send_message(last_chat_id, 'Choose your transport ⬇', reply_markup)
            else:
                schedule_bot.send_message(last_chat_id, 'Incorrect input! Try again 😔', False)
        else:
            last_chat_id = last_update['callback_query']['from']['id']
            text = last_update['callback_query']['data'] + ' was selected.'
            schedule_bot.send_popup_message(last_update['callback_query']['id'], text)
            '''

        new_offset = last_update_id + 1


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()
