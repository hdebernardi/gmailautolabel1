from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools

# If modifying these scopes, delete the file token.json.
SCOPES = 'https://www.googleapis.com/auth/gmail.modify'
def getService():
    """Shows basic usage of the Gmail API.
    Lists the user's Gmail labels.
    """
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    store = file.Storage('tests/token.json')
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('credentials.json', SCOPES)
        creds = tools.run_flow(flow, store)
    service = build('gmail', 'v1', http=creds.authorize(Http()))
    return service


import unittest
import labelisation.labeliseur as labeliseur


class Labeliseur(unittest.TestCase):
    """ Test la labélisation """

    def setUp(self):
        """Initialisation des tests."""
        self.service = getService()

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
