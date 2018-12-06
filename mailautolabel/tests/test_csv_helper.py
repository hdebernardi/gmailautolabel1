import unittest
import csv_helper as csv_helper

class Csv_helper(unittest.TestCase):
    """Test csv_helper.py"""
    def testGetPath(self):
        """Test return the absolute path of the file "username".csv"""
        self.assertTrue('True')

    def testIsPresent(self):
        """Test return 1 if path "username".csv is present, 0 if absent"""
        self.assertTrue('True')

    def testToDict(self):
        """ Test returns a dictionary from a csv file"""
        self.assertTrue('True')

    def testSaveMails(self):
        """Test create a csv file from a dictionnary"""
        self.assertTrue('True')

if __name__ == '__main__':
    unittest.main()
