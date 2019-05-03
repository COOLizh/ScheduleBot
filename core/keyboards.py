'''This module all kinds of buttons which will be used'''


def get_transport_keyboard():
    return {'inline_keyboard': [
            [{'text': '✈ Plane', 'callback_data': 'plane'}],
            [{'text': '🚄 Train', 'callback_data': 'train'}],
            [{'text': '🚈 Suburban', 'callback_data': 'suburban'}],
            [{'text': '🚌 Bus', 'callback_data': 'bus'}],
            [{'text': '⛵ Water transport', 'callback_data': 'water'}],
            [{'text': '🚁 Helicopter', 'callback_data': 'helicopter'}]]}
