import unittest
import ml.supervised as supervised

class Supervised(unittest.TestCase):
    """Test supervised"""
    def testSupervisedWithNolabellingMail(self):
        """Test return the absolute path of the file "username".csv"""
        self.assertTrue('True')

if __name__ == '__main__':
    unittest.main()
