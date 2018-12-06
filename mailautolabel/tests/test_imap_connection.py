import unittest
import extraction.imap.connection as connection

class Imap_Connection(unittest.TestCase):
    """Commenter"""

    def testOpen(self):
        """Test la connection"""
        self.assertTrue('True')

if __name__ == '__main__':
    unittest.main()
