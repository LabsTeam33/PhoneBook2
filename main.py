# coding=utf-8
import menu
import datamodel
import configparser


class Controller:
    """Контроллер ходу виконання програми """
    main_actions = ['Перегляд', 'Додавання',  'Вилучення', 'Модифікація', 'Пошук за номером', 'Пошук за значенням поля',
                    'Вихід']

    def __init__(self):
        self.flag = 0
        self.dbm = datamodel.DataModel()
        self.config = configparser.ConfigParser()
        self.config.read('settings.config')
        if not self.config.sections():
            self.config.read_dict({'Serialization': {'serializer': 'pickle'},
                                   'DataFiles': {'pickle': 'data.pickle',
                                                 'yaml': 'data.yaml',
                                                 'json': 'data.json'
                                                 }
                                   })
        serializer = self.config['Serialization']['serializer']
        self.file_path = self.config['DataFiles'][serializer]

        if serializer == 'json':
            self.serializer = datamodel.Serializer.json
        elif serializer == 'yaml':
            self.serializer = datamodel.Serializer.yaml
        else:
            self.serializer = datamodel.Serializer.pickle

        self.dbm.load(self.file_path, self.serializer)
        self.default_cols = ['імʼя', 'номер', 'місто', 'email']

    def show_all(self):
        """ Показати таблицю всіх записів """
        menu.print_table(self.dbm.get_table(), self.default_cols)

    def add_record(self):
        """ Інтерактивне додавання запису до бази"""
        record = menu.input_entity(self.dbm.record_keys)
        self.dbm.add_record(record)

    def delete_record(self):
        """ Інтерактивне видалення запису з бази"""
        table = self.dbm.get_table()
        index = menu.chose_entity('Виберіть номер елементу для видалення.', table, self.default_cols)
        self.dbm.delete_record(table[index]['номер'])

    def modify_record(self):
        """ Інтерактивни модифіказія запису"""
        table = self.dbm.get_table()
        index = menu.chose_entity('Виберіть номер елементу для модифікації.', table, self.default_cols)
        menu.print_table([table[index]], self.default_cols, head='Модифікується елемент')
        number = table[index]['номер']
        entity = self.dbm.get_record(number)
        self.dbm.delete_record(number)
        menu.change_entity(entity, self.dbm.record_keys)
        self.dbm.add_record(entity)

    def search(self, field):
        """ Інтерактивний пошук по записам бази за полем field
        :param field: поле для пошуку"""
        value = menu.input_field(field, str)
        table = self.dbm.search_by_field(field, value)
        menu.print_table(table, self.default_cols, head='Результати пошуку')

    def main_idle(self):
        """ Основний цикл спілкування з користувачем"""
        while self.flag == 0:
            action = menu.chose_one('Виберіть бажану дію:', self.main_actions)
            if action == 0:
                self.show_all()
            elif action == 1:
                self.add_record()
            elif action == 2:
                self.delete_record()
            elif action == 3:
                self.modify_record()
            elif action == 4:
                self.search('номер')
            elif action == 5:
                field = self.default_cols[menu.chose_one('Виберіть поле для пошуку', self.default_cols)]
                self.search(field)
            else:
                break
            self.flag = menu.chose_one(self.main_actions[action] + ' виконано. Бажаєте продовжити роботу?',
                                       ['Продовжити', 'Вийти'])
        self.dbm.save(self.file_path)


Controller().main_idle()
