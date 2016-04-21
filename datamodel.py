# coding=utf-8
import PickleSerializer
import YamlSerializer
import JsonSerializer
from enum import Enum
__author__ = 'supremist'


class Serializer(Enum):
    pickle = 1
    yaml = 2
    json = 3

    def get_serializer(self):
        if self == Serializer.pickle:
            return PickleSerializer.PickleSerializer
        elif self == Serializer.yaml:
            return YamlSerializer.YamlSerializer
        elif self == Serializer.json:
            return JsonSerializer.JsonSerializer
        else:
            raise ValueError


class DataModel:
    """ Менеджер для роботи з базою данних у файлі pickle"""
    record_keys = {'імʼя': '', 'номер': '', 'місто': '', 'email': ''}

    def __init__(self):
        self.records = {}

    def save(self, file_path, serializer=Serializer.pickle):
        serializer.get_serializer().save(file_path, self.records)

    def load(self, file_path, serializer=Serializer.pickle):
        data = serializer.get_serializer().load(file_path)
        if data:
            self.records = data

    def add_record(self, record):
        """ Додавання record до словнику записів
        :param record: запис-словник з полями record_keys для додавання"""
        rec = dict(record)
        number = rec.pop('номер')
        self.records[number] = rec

    def delete_record(self, number):
        """ Видалення запису з номером телефона number з бази
        :param number: номер телевона запису для видалення"""
        if number in self.records.keys():
            self.records.pop(number)

    def get_record(self, number):
        """ Отримання запису у вигляді словника з полями record_keys.
        Не превіряє наявність запису, якщо немає впевненості в наявності
        використовувати метод search_by_field
        :param number: номер телефона запису для отримання"""
        record = {'номер': number}
        record.update(self.records[number])
        return record

    def get_table(self):
        """ Отримання повного списку записів, кожен з яких у форматі словнику
         з полями record_keys"""
        table = []
        for number in sorted(self.records.keys()):
            table.append(self.get_record(number))
        return table

    def search_by_field(self, field, value):
        """ Пошук за полем field по записах в базі включаючи неповні входження value
        :param field: поле запису для пошуку
        :param value: шукане значення
        """
        table = []
        for number in sorted(self.records.keys()):
            record = self.get_record(number)
            if str(value) in str(record[field]):
                table.append(record)
        return table
