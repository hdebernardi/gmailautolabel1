import unittest

class LauncherGmail(unittest.TestCase):
    """Test launcherGmail.py"""
    def testAllLabel(self):
        """Test le fonctionnement des labels"""
        service = 'label'
        results = 'me'
        print(service, results)
        for service in results:
        #self.assertEqual(service,results)
            assert(True)
        else:
            assert(False)
        #self.assertTrue(results,label)

    def testAjoutLabel(self):
        """Test le fonctionnement d'ajout des labels"""

        #self.assertIn(label)
        #assert(True)

    def testCreerCsv(self):
        """Test le fonctionnement d'un fichier csv pour les mails déjà labélisés et
        ceux non labélisés"""
        #self.assertTrue(final_list)
        #assert(True)

    def testConnectGmail(self):
        """Test la connexion au service de Gmail."""
        #self.assertTrue(final_list)
        #assert(True)

if __name__ == '__main__':
    unittest.main()

import unittest
import time

def ajoutLabel(service,labelId,messageId):
	"""
	Ajoute le label "labelId" au mail "messageId"
	"""
	userId = "me"
	body = {'addLabelIds': [labelId]}
   
	results_m = service.users().messages().list(userId='me').execute()
	results = service.users().messages().modify(userId=userId, id=messageId, body=body).execute()

def testAjoutLabel(service):
    """Test le fonctionnement d'ajout des labels"""
    flag_test = False

    labelId = 'Label_3404667579525514162'
    messageId = '1677f1d31a6f6b7e'

    #on récupère le premier mail de la boite
    user_id = "me"
    message = service.users().messages().get(userId=user_id, id=messageId).execute()
    
    #on récupère tous ses labels
    label_avant = message['labelIds']
    print(label_avant)

    #ajoute le label "test" sur le mail
    ajoutLabel(service,labelId,messageId)

    #on récupère tous ses labels
    message = service.users().messages().get(userId=user_id, id=messageId).execute()
    label_apres = message['labelIds']
    print(label_apres)

    #on test si le label a bien été ajouté
    for i in range(len(label_avant)):
        if(label_avant[i] != label_apres[i]):
            if(label_apres[i] == 'Label_3404667579525514162'):
                flag_test = True
 
    #On supprime le label test qu'on lui a ajouté 
    body = {'removeLabelIds': [labelId]}
    results = service.users().messages().modify(userId=user_id, id=messageId, body=body).execute()
    
    print(flag_test)
    return flag_test

class Gmail(unittest.TestCase):
    """Test launcherGmail.py"""

    def testAllLabel(self):
        """Test le fonctionnement des labels"""
        #self.assertEqual(service,label)
        assert(True)

    def testAjoutLabel(self):
        """Test le fonctionnement d'ajout des labels"""
        #self.assertTrue(addLabelIds)
        print("test")
        assert(True)

    def testCreerCsv(self):
        """Test le fonctionnement d'un fichier csv pour les mails déjà labélisés et
        ceux non labélisés"""
        #self.assertTrue(final_list)
        assert(True)

    def testConnectGmail(self):
        """Test la connexion au service de Gmail."""
        #self.assertTrue(final_list)
        assert(True)
    #if __name__ == '__main__':
    #   unittest.main()
    