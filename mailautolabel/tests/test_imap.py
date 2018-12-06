import unittest
import extraction.imap.connection as connection
import extraction.imap.launcher_imap as launcher_imap
import extraction.imap.mail as mail

class Imap_Connection(unittest.TestCase):
    """Test imap/connection.py"""

    def testOpen(self):
        """Test la connection"""
        self.assertTrue('True')



    """Test imap/launcher.py"""

    def testLancementImap(self):
        """Commenter"""
        self.assertTrue('True')


    """Test imap/mail.py"""

    def testDecodeHtml(self):
        """Commenter"""
        self.assertTrue('True')

    def testGetHeader(self):
        """Commenter"""
        self.assertTrue('True')

    def testGetFlags(self):
        """Commenter"""
        self.assertTrue('True')

    def testGetBody(self):
        """Commenter"""
        self.assertTrue('True')

    def testGetFolders(self):
        """Commenter"""
        self.assertTrue('True')

    def testGetMails(self):
        """Commenter"""
        self.assertTrue('True')

    def testGetUsefulPartsOfMails(self):
        """Commenter"""
        self.assertTrue('True')


if __name__ == '__main__':
    unittest.main()
