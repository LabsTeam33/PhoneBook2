# coding=utf-8
import json


class JsonSerializer:

    @staticmethod
    def load(file_path):
        """
        Load serialized data from file_path file
        :param file_path: path to data file
        :return: if success return loaded data, else None
        """
        try:
            with open(file_path, 'r') as file:
                return json.load(file)
        except IOError:
            print('Файл не знайдено. Буде створена нова база.')

    @staticmethod
    def save(file_path, data):
        """
         Serialize data to file_path file. File will be rewrite.
         :param file_path: path to data file
         :param data: serializable object
         :return: None
         """
        with open(file_path, 'w') as file:
            json.dump(data, file)
