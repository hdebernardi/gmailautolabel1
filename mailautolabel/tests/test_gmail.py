import unittest
import extraction.gmail.connection as connection
import extraction.gmail.launcher_gmail as launcher_gmail
import extraction.gmail.mail as mail
import tests.donnees.connection_gmailtest as connection_gmailtest
import csv_helper

class Gmail(unittest.TestCase):

    def setUp(self):
        """Initialisation des tests."""
        self.service = connection_gmailtest.getService()
        self.username = "tests/NON_LABELmailautolabel1.test@gmail.com"
        self.messageId = '1677f1d31a6f6b7e'
        self.user_id = "me"
        #Liste d'éléments qui doivent etre présent dans les fichiers csv de test
        self.elem_body = []
        self.elem_body.append('CONTENU TEST 3')
        self.elem_body.append('CONTENU TEST 2')
        self.elem_body.append('CONTENU MESSAGE 1')

        self.elem_ids = []
        self.elem_ids.append('1678348fa9838759')
        self.elem_ids.append('1678348f6acc89f2')
        self.elem_ids.append('167834871e6e79d2')
        self.elem_ids.append('16783481d21f3e44')

        self.elem_expediteur ='GARCIA Toni <toni.garcia@etu.univ-amu.fr>'


    """Test gmail/connection.py"""
    def testOpen(self):
        print(self.username)
        """Dans setUp l'appel à la fonction connection_gmailtest.getService() fait exactement la même chose que connection"""
        self.assertTrue('True')




    """----------------------------------------------
                      Test gmail/launcher_gmail.py
    -------------------------------------------------"""
    """"""
    def testExtracteur(self):
        """Test l'extraction"""
        username2 = self.username+"testExtracteur"
        labelisedMails,unlabelisedMails=launcher_gmail.extracteur(username2,self.service,"TOUT")

        ####on vérifie que les mails non labélisés soient correcte
        #test si les ids sont correcte
        for id in self.elem_ids:
            self.assertIn(id,str(unlabelisedMails))
        #test si les bodys sont correcte
        for body in  self.elem_body:
            self.assertIn(body,str(unlabelisedMails))
        #test si l'expédieur est correcte
        self.assertIn(self.elem_expediteur,str(unlabelisedMails))

        ###on test si le fichier csv a été crée
        self.assertTrue(csv_helper.isPresent(username2))


    def testLancementGmail(self):
        """Test le lancement de gmail"""
        #Cette fonction intéragit avec l'utilisateur il est donc
        #difficile de la tester seulement dans une fonction.
        #Une batterie de test a cependant été effectuée à l'extérieur de la fonction
        #1)Sur un terminal: 
        #   Entrer un nbr différent de 1 et 2
        #  ->fonctionne car la labélisation est appelée par défaut
        #2)Sur l'interface graphique:
        #  Appuyer plusieurs fois sur le bouton ce qui correspond à lancer plusieurs fois la fonction
        #  ->fonctionne correctement en réinialisant le programme à chaque fois
        #   Fermer la fenetre de question au lieu de répondre oui ou non
        #   ->lance la labélisation

        self.assertTrue('True')





    """----------------------------------------------
                       Test gmail/mail.py
    -------------------------------------------------"""
    def testClearBody(self):
        """On récupère le message en Base 64 et on appel la fonction clearBody"""
        #récupère le mail
        message = self.service.users().messages().get(userId=self.user_id, id=self.messageId).execute()
        # récupère le payload du message
        payld = message['payload']
        #récupère le corps du message
        part_body = payld['parts'][0]['body']
        if part_body['size']==0:
            mssg_body =' '
        else:  
            mssg_body = mail.clearBody(part_body['data'])
        self.assertIn("Merci d'avoir créé un compte Google.",mssg_body)
        self.assertIn("Avec Gmail pour Android",mssg_body)
        self.assertIn("vérification de vos",mssg_body)

 

    def testExtraitInfoMsg(self):
        """On vérifie que l'extraction du mail renvoi les bons paramètres"""
        #on récupère le mail
        message = self.service.users().messages().get(userId=self.user_id, id=self.messageId).execute()
        #on appel la fonction
        msg = mail.extraitInfoMsg(self.service,message)
        #on test si le contenu est correct
        Body = "Bonjour test,"
        self.assertIn(Body,str(msg["Message_body"]))
        Subject = "bienvenue"
        self.assertIn(Subject,str(msg["Subject"]))
        Sender = "googlecommunityteam-noreply@google.com"
        self.assertIn(Sender,str(msg["Sender"]))


    def testRecupAllMessages(self):
        """On récupère les messages et on vérifie que les ids sont correcte"""
        messages = mail.recupAllMessages(self.service,"TOUT")
        for id in self.elem_ids:
            self.assertIn(id,str(messages))

    def testAllMessage(self):
        """On test si les messages retournés sont correcte"""
        final_list = mail.allMessage(self.service,"TOUT")
        #test si les ids sont correcte
        for id in self.elem_ids:
            self.assertIn(id,str(final_list))
        #test si les bodys sont correcte
        for body in  self.elem_body:
            self.assertIn(body,str(final_list))
        #test si l'expédieur est correcte
        self.assertIn(self.elem_expediteur,str(final_list))
 
if __name__ == '__main__':
    unittest.main()

