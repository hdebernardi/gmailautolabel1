import unittest
import ml.supervised as supervised

class Supervised(unittest.TestCase):
    """Test supervised"""
    def testSupervisedWithNolabellingMail(self):
        """Test la fonction de machine learning"""
        #test fait "manuellement"

        ####Les cas traités générant des erreurs
        #ML sur une boite mail non triés (fichier username.csv est vide)
        #ML sur une boite mail sans mails a labélisé (fichier NON_LABELusername.csv vide)
        #ML sur une boite sans label
        #ML sur une boite avec un seul label

        ####Le cas fonctionnant
        #ML sur une boite mail triés avec des mails pas encore labélisés

if __name__ == '__main__':
    unittest.main()
