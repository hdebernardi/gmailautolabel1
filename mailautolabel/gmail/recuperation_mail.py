from gmail.extraction_info_mail import *
import re

#######################################################################
#               Récupère tous les mails lablélisé, extrait les infos  #  
#                    et les stocke dans une liste                     #
#######################################################################

def recupAllMessages(service):
    """
    Récupère tous les mails de la boite
    """
        
    print("On récupère tous les messages de la boite mail")
    user_id = 'me'

    # On récupère tous les messages
    response = service.users().messages().list(userId='me').execute()
    messages = []
    if 'messages' in response:
      messages.extend(response['messages'])

    while 'nextPageToken' in response:
      page_token = response['nextPageToken']
      response = service.users().messages().list(userId='me', pageToken=page_token).execute()
      messages.extend(response['messages'])
      
    print("Nombre total de mail: ",len(messages))
    return messages


def allMessage(service):
    """
    Parcourt tous les messages de la boite mail.
    Si la case 'Folder' est == à False cela signifie que le mail n'est pas labélisé on ne l'ajoute donc pas à la liste final.
    On retourne la liste finale
    """
        
    user_id = 'me'
    messages = recupAllMessages(service = service)

    final_list = [ ]

    print("On extrait les informations pour chaque mails")
    # On parcourt chaque message
    i=0
    for mssg in messages:
        print("Extraction des info du message ",i)
        i+=1
        message = service.users().messages().get(userId=user_id, id=mssg['id']).execute()
        temp_dict = extraitInfoMsg(service=service,message=message)
        final_list.append(temp_dict)

    return final_list
