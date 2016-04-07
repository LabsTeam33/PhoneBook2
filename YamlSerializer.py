# coding=utf-8
import yaml


class YamlSerializer:

    @staticmethod
    def load(file_path):
        try:
            with open(file_path, 'rb') as file:
                return yaml.load(file)
        except IOError:
            print('Файл не знайдено. Буде створена нова база.')

    @staticmethod
    def save(file_path, data):
        with open(file_path, 'wb') as file:
            yaml.dump(data, file)