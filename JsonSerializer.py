# coding=utf-8
import json


class JsonSerializer:

    @staticmethod
    def load(file_path):
        try:
            with open(file_path, 'r') as file:
                return json.load(file)
        except IOError:
            print('Файл не знайдено. Буде створена нова база.')

    @staticmethod
    def save(file_path, data):

        with open(file_path, 'w') as file:
            json.dump(data, file)
