import unittest 

from test_code import get_formated_name

class NamesTestCase(unittest.TestCase):
    def test_first_last_name(self):
        formatted_name = get_formated_name('Asaf','Aviv')
        self.assertEqual(formatted_name,'Asaf Aviv')

unittest.main()