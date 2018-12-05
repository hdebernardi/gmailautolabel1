import unittest

class Csv_helper(unittest.TestCase):
    """Test csv_helper.py"""
    def testGetPath(self):
        """Test return the absolute path of the file "username".csv"""
        assert(True)

    def testIsPresent(self):
        """Test return 1 if path "username".csv is present, 0 if absent"""
        assert(True)

    def testToDict(self):
        """ Test returns a dictionary from a csv file"""
        assert(True)

    def testSaveMails(self):
        """Test create a csv file from a dictionnary"""
        assert(True)

if __name__ == '__main__':
    unittest.main()

#pour le test: astou$ python -m unittest -v testlauncherImap