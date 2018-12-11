from __future__ import print_function
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
from apiclient import errors
import email

# Si vous modifiez ces `SCOPES`, supprimez le fichier `token.json`.
SCOPES = 'https://www.googleapis.com/auth/gmail.modify'

###########################################################################
#On se connecte au service de gmail
def open():
    '''
    -Ouvre une connection vers une boite mail.
    -Paramètres
        -``hostname`` : nom du serveur auquel nous voulons nous connecter (ex : gmail, aol).
        -``username`` : identifiant de l'utilisateur de la boite mail.
        -``password`` : mot de passe de l'utilisateur de la boite mail.
    -Retourne la connexion avec le serveur en GMAIL.
    '''
    
    print("CONNEXION AU SERVEUR DE GMAIL")
    store = file.Storage('extraction/gmail/configuration_files/token.json')
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('extraction/gmail/configuration_files/credentials.json', SCOPES)
        creds = tools.run_flow(flow, store)
    service = build('gmail', 'v1', http=creds.authorize(Http()))
    return service
