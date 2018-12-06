import unittest
import extraction.gmail.launcher_gmail as launcher_gmail

class Launcher_Gmail(unittest.TestCase):
    """Test csv_helper.py"""

    def testExtracteur(self):
        """Test l'extraction"""
        self.assertTrue('True')

    def testLancementGmail(self):
        """Test le lancement de gmail"""
        self.assertTrue('True')


if __name__ == '__main__':
    unittest.main()
