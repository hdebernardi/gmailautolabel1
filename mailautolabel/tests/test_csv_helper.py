import unittest
import csv_helper
import csv

class Csv_helper(unittest.TestCase):
    def setUp(self):
        """Initialisation des tests."""
        self.username = "tests/NON_LABELmailautolabel1.test@gmail.com"
        #Liste d'éléments qui doivent etre présent dans les fichiers csv de test
        self.elem_present = []
        self.elem_present.append('CONTENU TEST 3')
        self.elem_present.append('CONTENU TEST 2')
        self.elem_present.append('CONTENU MESSAGE 1')

        self.elem_present.append('GARCIA Toni <toni.garcia@etu.univ-amu.fr>')
        self.elem_present.append('1678348fa9838759')
        self.elem_present.append('1678348f6acc89f2')
        self.elem_present.append('167834871e6e79d2')
        self.elem_present.append('16783481d21f3e44')


    """Test csv_helper.py"""
    def testGetPath(self):
        """On vérifie que le chemin du fichier contient les bonnes partie"""
        chemin_fich = csv_helper.getPath(self.username)
        chemin_attendu = "mailautolabel/data/"+self.username
        self.assertIn(chemin_attendu,chemin_fich)

    def testIsPresent(self):
        """On test si le fichier est présent, puis si un faux fichier est absent"""
        isPresent = csv_helper.isPresent(self.username) 
        self.assertTrue(isPresent)
        isPresent = csv_helper.isPresent(self.username+"2") 
        self.assertFalse(isPresent)

    def testToDict(self):
        """On vérifie le contenu du csv avec nos données"""
        #contenu du csv
        contenu_csv = csv_helper.toDict(self.username)
        #on test si des elements des mails sont bien présent dans le contenu_csv
        for elem in self.elem_present:
            self.assertIn(elem,str(contenu_csv))


    def testSaveMails(self):
        """On vérifie que le csv est bien crée et qu'il a le bon contenu"""
        #on crée le fichier csv
        username2= self.username+"_testSaveMails"
        csv_helper.saveMails(username2,self.elem_present)
        #on l'ouvre et on vérifie son contenu
        with open(csv_helper.getPath(username2), newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                self.assertIn(row["0"],str(self.elem_present))


if __name__ == '__main__':
    unittest.main()
