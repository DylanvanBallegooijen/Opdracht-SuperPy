import unittest
from datetime import datetime
from functions.date import convert_to_date


class Test(unittest.TestCase):

    def test(self):
        assert convert_to_date('2022') == datetime(2021, 1, 1, 0, 0)
        assert convert_to_date('2022-05') == datetime(2021, 5, 1, 0, 0)
        assert convert_to_date('2022-05-25') == datetime(2021, 5, 25, 0, 0)

        self.assertRaises(ValueError, convert_to_date, '2022-04-32')
        self.assertRaises(ValueError, convert_to_date, '2021-14-02')
        self.assertRaises(ValueError, convert_to_date, '')
