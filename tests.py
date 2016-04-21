import unittest
from unittest.mock import patch
import datamodel


class BaseTestClass(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.test_dict0 = {'імʼя': 'test_name', 'номер': '12345',
                          'місто': 'test_city', 'email': 'test_email'}
        cls.test_dict1 = {'імʼя': 'test_name1', 'номер': '1111',
                          'місто': 'test_city1', 'email': 'test_email1'}
        cls.test_records_added = {'12345': {
                                       'імʼя': 'test_name',
                                       'місто': 'test_city',
                                       'email': 'test_email'},
                                  '1111': {'імʼя': 'test_name1',
                                           'місто': 'test_city1',
                                           'email': 'test_email1'}}

    def setUp(self):
        self.dbm = datamodel.DataModel()
        self.dbm.records = {'1111': {'імʼя': 'test_name1',
                                     'місто': 'test_city1',
                                     'email': 'test_email1'}}

    def test_add_record(self):
        self.dbm.add_record(self.test_dict0)
        self.assertEqual(self.test_records_added, self.dbm.records)

    @patch('builtins.open')
    @patch('pickle.load')
    def test_load(self, mock_load, mock_open):
        mock_load.return_value = self.test_dict0
        self.dbm.load('')
        self.assertEqual(self.test_dict0, self.dbm.records)

    def test_delete_record(self):
        self.dbm.delete_record(self.test_dict1['номер'])
        self.assertEqual({}, self.dbm.records)

    def test_get_record(self):
        self.assertEqual(self.test_dict1,
                         self.dbm.get_record(self.test_dict1['номер']))

    def test_get_table(self):
        self.dbm.records = self.test_records_added
        self.assertEqual([self.test_dict1,
                          self.test_dict0], self.dbm.get_table())

    def test_search_by_field(self):
        self.assertEqual([self.test_dict1],
                         self.dbm.search_by_field('номер', '11'))


if __name__ == '__main__':
    unittest.main()
