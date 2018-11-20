from __future__ import print_function
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
import email
from apiclient import errors


from gmail.RecuperationMail import *
import csv_helper

# If modifying these scopes, delete the file token.json.
SCOPES = 'https://www.googleapis.com/auth/gmail.modify'

#######################################################################
#   Affiche tous les labels deja creer de la boite gmail              #
#######################################################################
def AllLabel(service):
    print('---------------------------------------------------')
    print('LABELS PRESENT SUR LA BOITE MAIL:')
    # Call the Gmail API
    results = service.users().labels().list(userId='me').execute()
    labels = results.get('labels', [])

    if not labels:
        print('No labels found.')
    else:
        print('Labels:')
        for label in labels:
            print(label['name'],label['id'])


#######################################################################
#                Ajout d'un label a un mail                           #
#######################################################################
def AjoutLabel(service,labelId,messageId):
	userId = "me"
	body = {'addLabelIds': [labelId]}
   
	results_m = service.users().messages().list(userId='me').execute()
	results = service.users().messages().modify(userId=userId, id=messageId, body=body).execute()


#######################################################################
#  			 Fonction principale                          #
#######################################################################

def connectGmail(username):
    """Shows basic usage of the Gmail API.
    Lists the user's Gmail labels.
    """
    store = file.Storage('token.json')
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('credentials.json', SCOPES)
        creds = tools.run_flow(flow, store)
    service = build('gmail', 'v1', http=creds.authorize(Http()))
   
    # Ajoute le label UNREAD au premier mail
    #sujet du message : Kevin, vous avez 46 nouvelles notification
    #AjoutLabel(service = service,labelId = 'UNREAD',messageId = '167329c4039358c9' )

    final_list = AllMessage(service=service)
    csv_helper.save_mails(username, final_list)


