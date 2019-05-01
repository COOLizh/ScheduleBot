from core.schedule_bot import ScheduleBot
import datetime
from core.keyboards import *


def main():
    token = '826030216:AAEOSvYrw1V5-q4vBbS-h8l81s-jEwz52AE'
    schedule_bot = ScheduleBot(token)
    now = datetime.datetime.now()
    new_offset = None
    today = now.day
    hour = now.hour

    while True:
        schedule_bot.get_updates(new_offset)

        last_update = schedule_bot.get_last_update()

        last_update_id = last_update['update_id']
        last_chat_id = last_update['callback_query']['from']['id']

        reply_markup = get_transport_keyboard()

        schedule_bot.send_message(last_chat_id, 'Choose your transport. Last choice: ' + last_update['callback_query']['data'], reply_markup)

        new_offset = last_update_id + 1


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()
