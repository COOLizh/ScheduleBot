'''The main module of project'''
import core.mongodb as mongo
from handlers.schedule_bot import ScheduleBot
from core.keyboards import *


def update(schedule_bot, new_offset):
    '''This method checks new updates in bot and return needful variables'''
    schedule_bot.get_updates(new_offset)
    last_update = schedule_bot.get_last_update()
    if 'message' in last_update.keys():
        last_update_id = last_update['update_id']
        last_sent_text = last_update['message']['text']
        last_chat_id = last_update['message']['chat']['id']
        return last_update_id, last_sent_text, last_chat_id

    elif 'callback_query' in last_update.keys():
        last_chat_id = last_update['callback_query']['from']['id']
        last_update_id = last_update['update_id']
        key = last_update['callback_query']['data']
        return last_chat_id, last_update_id, key


def get_schedule(schedule_bot, last_chat_id, last_update_id, method):
    '''This function send to user schedule on station'''
    exit = True if method == 'Schedule on station 🚏' else False
    while True:
        schedule_bot.send_message(last_chat_id, 'Enter the name of station ✏', False)

        new_offset = last_update_id + 1
        last_update_id, last_sent_text, last_chat_id = update(schedule_bot, new_offset)

        text = 'List of found stations 🔎\n'
        stations, codes = schedule_bot.find_stations(last_sent_text)
        count = len(stations)
        reply_markup = get_sc_keyboard(count, codes)

        if count == 0:
            text = 'No station found ☹'
            schedule_bot.send_message(last_chat_id, text, False)
            return
        else:
            for i in range(count):
                text += str(i + 1) + '. ' + stations[i] + '\n'
            text += 'Select the station number you need ⬇'
            schedule_bot.send_message(last_chat_id, text, reply_markup)

        # searching by station
        new_offset = last_update_id + 1
        last_chat_id, last_update_id, key = update(schedule_bot, new_offset)
        if not exit:
            first_key = key
            exit = True
        else:
            break

    if method == 'Schedule on station 🚏':
        schedule_bot.send_message(last_chat_id, schedule_bot.get_station_schedule(key), False)
    else:
        schedule_bot.send_message(last_chat_id, schedule_bot.get_stations_schedule(first_key, key), False)


def main():
    token = '826030216:AAEOSvYrw1V5-q4vBbS-h8l81s-jEwz52AE'
    schedule_bot = ScheduleBot(token)
    mongo.create_db_codes()
    new_offset = None

    while True:
        last_update_id, last_sent_text, last_chat_id = update(schedule_bot, new_offset)

        if last_sent_text == '/start':
            reply_markup = get_methods_keyboard()
            schedule_bot.send_message(last_chat_id, 'Choose method in your keyboard.', reply_markup)
            new_offset = last_update_id + 1

        # depening on method start this method
        elif last_sent_text == 'Schedule on station 🚏' or last_sent_text == 'Schedule behind stations 🚏 ➡ 🚏':
            get_schedule(schedule_bot, last_chat_id, last_update_id, last_sent_text)
            new_offset = last_update_id + 1

        else:
            schedule_bot.send_message(last_chat_id, 'Incorret input ‼ Choose the method in keyboard ‼', False)
            new_offset = last_update_id + 1


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()
