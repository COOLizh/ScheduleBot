from core.schedule_bot import ScheduleBot
import datetime
from telegram import InlineKeyboardButton, InlineKeyboardMarkup


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
        last_chat_text = last_update['message']['text']
        last_chat_id = last_update['message']['chat']['id']
        last_chat_name = last_update['message']['chat']['username']

        if last_chat_text == 's':
            reply_markup = {
            "inline_keyboard": [
                [
                    {"text": "Yes", "url": "http://www.google.com/" , 'callback_data' : '1'},
                    {"text": "No", "url": "http://www.google.com/"}
                ]
            ]
        }

            #s = schedule_bot.get_station_schedule('bus')
            schedule_bot.send_message(last_chat_id, ';)', reply_markup)

        new_offset = last_update_id + 1


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()
