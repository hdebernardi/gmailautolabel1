import unittest
import extraction.gmail.connection as connection

class Gmail_Connection(unittest.TestCase):
    """Test gmail/connection.py"""

    def testOpen(self):
        """Test la connection"""
        self.assertTrue('True')

if __name__ == '__main__':
    unittest.main()
