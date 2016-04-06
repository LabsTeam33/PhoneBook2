# coding=utf-8
__author__ = 'supremist'
""" Модуль для інтерактивного спілкування з користувачем через консоль"""


def print_menu(items):
    """ Друкує меню з пунктів items
    :param items: список пунктів для друку"""
    for index, item in enumerate(items):
        print(str(index) + ') ' + item)


def request(max_index):
    """ Отримує з потоку вводу значення, доки не буде введено число від 0 до max_index. Повертає значення числа.
    :param max_index: максимально можливе для вводу число"""
    result = -1
    while True:
        try:
            result = int(input('Введіть номер пункту меню: '))
        except ValueError:
            print('Ви ввели не число.')
        else:
            if 0 <= result < max_index:
                break
            else:
                print('Ви вибрали неіснуючий пункт.')
    return result


def chose_one(head, items):
    """ Друкує меню з пунктів items та заголовком head. Інтерактивно отримує номер пункту та поертає його.
    :param head: строка заголовок меню
    :param items: список пунктів меню"""
    print(head)
    print_menu(items)
    return request(len(items))


def chose_entity(head, items, cols, col_width=20):
    """ Друкує таблицю з items, cols та col_width. Виводить head та повертає отриманий
    від користувача номер рядка в таблиці.
    :param head: заголовок для друку
    :param items: список словників, що друкуєсться таблицею
    :param cols: колонки таблиці
    :param col_width: ширина однієї колонки"""
    print_table(items, cols, colwidth=col_width)
    print(head)
    return request(len(items))


def print_table(rows, cols, head='', colwidth=20):
    """ Друкує таблицю з рядкам rows, колонками cols, шириною колонки col_width та заголовком head.
    :param rows: список словників, що друкуєсться таблицею
    :param cols: колонки таблиці
    :param head: заголовок таблиці
    :param colwidth: ширина однієї колонки"""
    print(head)
    if not rows or not cols:
        print('Список пустий')
        return
    separator = '+----+' + ('-' * colwidth + '+') * len(cols)
    print(separator)
    row_str = '|    |'
    for col_name in cols:
        row_str += ('{0:' + str(colwidth) + '}|').format(col_name)
    print(row_str)
    print(separator)
    for index, row in enumerate(rows):
        row_str = '|{0:4}|'.format(index)
        for col in cols:
            ln = len(str(row[col]))
            row_str += str(row[col]) + ' '*(colwidth-ln) + '|'
        print(row_str)
    print(separator)


def input_entity(keys):
    """ Повертає словник з ключами keys, полями такого ж типу, як поля keys
    :param keys: словник приклад"""
    entity = {}
    for key in keys.keys():
        entity[key] = input_field(key, type(keys[key]))
    return entity


def input_field(name, field_type):
    """
    Повертає значення поля name типу field_type з потоку вводу.
    :param name: імʼя поля для вводу
    :param field_type: тип поля
    :return: введене значення типу field_type
    """
    value = None
    while True:
        try:
            value = field_type(input('Введіть поле %s:' % name))
        except ValueError:
            print('Невірний тип поля.')
        else:
            break
    return value


def change_entity(entity, keys):
    """
    Змінює словник entity згідно з введеними значеннями.
    :param entity: словник, що змінюється
    :param keys: словник приклад з ключами значення яких буде змінюватися у entity та буде такого ж типу,
    як і тип значення цього ключа в keys
    :return:
    """
    for key in keys.keys():
        print(key + ': ' + str(entity[key]))
        entity[key] = input_field(key, type(keys[key]))
