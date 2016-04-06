# coding=utf-8
import pickle


class PickleSerializer:

    @staticmethod
    def load(file_path):
        try:
            with open(file_path, 'rb') as file:
                return pickle.load(file)
        except IOError:
            print('Файл не знайдено. Буде створена нова база.')

    @staticmethod
    def save(file_path, data):
        with open(file_path, 'wb') as file:
            pickle.dump(data, file)
