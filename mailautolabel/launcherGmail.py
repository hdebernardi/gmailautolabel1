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
def AjoutLabel(service):
	labelId = "UNREAD"
	userId = "me"
    
	body = {'addLabelIds': [labelId]}
   
	results_m = service.users().messages().list(userId='me').execute()
	messages = results_m.get('messages', [])
	#for message in messages:
	messageId = messages[0]['id']
	results = service.users().messages().modify(userId=userId, id=messageId, body=body).execute()


#######################################################################
#              Affiche le nb de messages dans la boite mail           #
#######################################################################
def NbMsg(service):
    i = 0

    response = service.users().messages().list(userId='me').execute()
    messages = []
    if 'messages' in response:
      messages.extend(response['messages'])

    while 'nextPageToken' in response:
      page_token = response['nextPageToken']
      response = service.users().messages().list(userId='me', pageToken=page_token).execute()
      messages.extend(response['messages'])

    for mssg in messages:
        i+=1
    print("nb message = ",i)
    sys.exit(0)

#######################################################################
#  			 Fonction principale                          #
#######################################################################

def LanceTout(service):
    print("on lance tout")
    # Ajoute le label UNREAD au premier mail
    #AjoutLabel(service=service)

    #affiche tous les labels
    #AllLabel(service=service)

    #affiche le nb de mail sur la boite mail
    #NbMsg(service = service)

    #affiche tous les mails
    #final_list = AllMessage(service=service)
    #afficheList(final_list=final_list)

    #affiche tous les mails non labélisés
    #final_list = MessagesNonLabelelises(service=service) 
    #afficheList(final_list=final_list)



def connectGmail(username):
    """Shows basic usage of the Gmail API.
    Lists the user's Gmail labels.
    """
    store = file.Storage('token.json')
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('mailautolabel/gmail/credentials.json', SCOPES)
        creds = tools.run_flow(flow, store)
    service = build('gmail', 'v1', http=creds.authorize(Http()))

    #LanceTout(service=service)    
    final_list = AllMessage(service=service)
    csv_helper.save_mails(username, final_list)


