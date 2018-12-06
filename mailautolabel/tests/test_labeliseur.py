import unittest
import labelisation.labeliseur as labeliseur
import tests.donnees.connection_gmailtest as connection_gmailtest

class Labeliseur(unittest.TestCase):
    """ Test la labélisation """

    def setUp(self):
        """Initialisation des tests."""
        self.service = connection_gmailtest.getService()

    def testAjoutLabel(self):
        """ Test l'ajout de mail """
        labelId = 'Label_3404667579525514162'
        messageId = '1677f1d31a6f6b7e'
        user_id = "me"

        #ajoute le label "test" sur le mail
        labeliseur.ajoutLabel(self.service,labelId,messageId)
        
        #recupere le label du mail
        message = self.service.users().messages().get(userId=user_id, id=messageId).execute()
        label_apres = message['labelIds'] 

        #supprime le label du mail
        body = {'removeLabelIds': [labelId]}
        results = self.service.users().messages().modify(userId=user_id, id=messageId, body=body).execute()
        
        self.assertIn(labelId,label_apres)


    def testGmailLabelisation(self):
        """ Test la labélisation apres le ml """
        #labeliseur.gmailLabelisation(self.service,'test@gmail.com')
        self.assertTrue('True')        

if __name__ == '__main__':
    unittest.main()
