'''This module all kinds of buttons which will be used'''


def get_sc_keyboard(count):
    '''This functions returns station choice of user'''
    if count <= 5:
        keyboard = {'inline_keyboard': [[{'text': f'{i + 1}', 'callback_data': f'{i}'} for i in range(count)]]}
        return keyboard
    else:
        num = count // 5
        ost = count % 5
        ch = 6
        keyboard = {'inline_keyboard': [[{'text': f'{i + 1}', 'callback_data': f'{i}'} for i in range(5)]]}
        for i in range(num - 1):
            keyboard['inline_keyboard'].append([{'text': f'{ch + i}', 'callback_data': f'{ch + i - 1}'} for i in range(5)])
            ch += 5
        keyboard['inline_keyboard'].append([{'text': f'{ch + i}', 'callback_data': f'{ch + i - 1}'} for i in range(ost)])
        return keyboard


def get_transport_keyboard():
    '''This functon returns inline kyeboard of chosen tupe of transport'''
    return {'inline_keyboard': [
        [{'text': '✈ Plane', 'callback_data': 'plane'}],
        [{'text': '🚄 Train', 'callback_data': 'train'}],
        [{'text': '🚈 Suburban', 'callback_data': 'suburban'}],
        [{'text': '🚌 Bus', 'callback_data': 'bus'}],
        [{'text': '⛵ Water transport', 'callback_data': 'water'}],
        [{'text': '🚁 Helicopter', 'callback_data': 'helicopter'}]]}
