from __future__ import print_function
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
from apiclient import errors
import email

from gmail.recuperation_mail import *
import ml.supervised
import csv_helper

# Si vous modifiez ces `SCOPES`, supprimez le fichier `token.json`.
SCOPES = 'https://www.googleapis.com/auth/gmail.modify'

#######################################################################
#   Affiche tous les labels deja créés de la boite gmail              #
#######################################################################
def allLabel(service):
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
def ajoutLabel(service,labelId,messageId):
	"""
	Ajoute le label "labelId" au mail "messageId"
	"""
	userId = "me"
	body = {'addLabelIds': [labelId]}
   
	results_m = service.users().messages().list(userId='me').execute()
	results = service.users().messages().modify(userId=userId, id=messageId, body=body).execute()



def creerCsv(username,service):
        """
        Créer un fichier csv pour les mails déjà labélisés et
        ceux non labélisés
        """
        #on crée le fichier csv pour les mails déjà labélisés
        final_list = allMessage(service)
        csv_helper.saveMails(username, final_list)
        #on crée le fichier csv pour les mails non labélisés
        final_list = messagesNonLabelises(service)
        csv_helper.saveMails("NON_LABEL"+username, final_list)


#######################################################################
#  			 Fonction principale                          #
#######################################################################
def connectGmail(username):
    """
    Ce connecte au service de Gmail.
    Si c'est la première connection de l'utilisateur, crée un fichier csv pour les mails labélisés et non labélisés.
    Si ce n'est pas la première connection, soit on réentraine le modèle, soit on appelle la fonction de ML et on labélise les mails.
    """
    #On se connecte au service de gmail
    store = file.Storage('token.json')
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('credentials.json', SCOPES)
        creds = tools.run_flow(flow, store)
    service = build('gmail', 'v1', http=creds.authorize(Http()))
   

    #Si aucun fichier csv n'est crée pour username, c'est une première connection
    if(csv_helper.isPresent(username) == 0):
        print("Première connection")
        creerCsv(username,service)
    #Sinon on propose deux choix à l'utilisateur
    else:
        choix=input("Désirez-vous:\n réentrainer votre IA (Taper 1)\n Labéliser vos mails (Taper 2)\n Saisir:")
        #Réentrainer l'IA
        if(choix == "1"):
            creerCsv(username,service)
        #Labéliser les mails
        else:
            print("--------------------------------------")
            print("MACHINE LEARNING")
            mails_nonlab = csv_helper.toDict("NON_LABEL"+username)
            prediction = ml.supervised.supervisedWithNolabellingMail(username)
            print("--------------------------------------")
            print("Labélisation des mails en cours")
            for i in range(len(prediction)):
                ajoutLabel(service = service,labelId = prediction[i],messageId = mails_nonlab[i]['id'])

    
