from core.bot_handler import BotHandler
import datetime


def main():
    token = '826030216:AAEOSvYrw1V5-q4vBbS-h8l81s-jEwz52AE'
    queue_bot = BotHandler(token)
    now = datetime.datetime.now()
    new_offset = None
    today = now.day
    hour = now.hour

    while True:
        queue_bot.get_updates(new_offset)

        last_update = queue_bot.get_last_update()

        last_update_id = last_update['update_id']
        last_chat_text = last_update['message']['text']
        last_chat_id = last_update['message']['chat']['id']
        last_chat_name = last_update['message']['chat']['username']

        if last_chat_text == '/schedule':
            pass

        new_offset = last_update_id + 1


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()
