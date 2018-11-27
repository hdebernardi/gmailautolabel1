from gmail.ExtractionInfoMail import *
import re

#######################################################################
#               Récupère tous les mails lablélisé, extrait les infos  #  
#                    et les stockent dans une liste                   #
#######################################################################

def RecupAllMessages(service):
    """
    Récupère tous les mails de la boite
    """
        
    print("On récupère tous les messages de la boite mail")
    user_id =  'me'

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

def AllMessage(service):
    """
    Parcourt tous les messages de la boite mail.
    Si la case 'Folder' est == à False cela signifie que le mail n'est pas  labélisé on ne l'ajoute donc pas à la liste final.
    On retourne la liste finale
    """
        
    user_id = 'me'
    messages = RecupAllMessages(service = service)

    final_list = [ ]

    print("On extrait les informations pour chaque mails")
    # On parcourt chaque message
    i=0
    for mssg in messages:
        print("Extraction info message ",i)
        i+=1
        message = service.users().messages().get(userId=user_id, id=mssg['id']).execute()
        temp_dict = ExtraitInfoMsg(service=service,message=message)

        #Si le mail n'est pas labélisé on ne l'ajoute pas 
        if(temp_dict['Folder'] == 'False'):
            pass
        #sinon on l'ajoute
        else:
            final_list.append(temp_dict)

    return final_list

#######################################################################
#         Récupère tous les mails non labelisés, extrait les infos    #
#             et les stockent dans une liste                          #
#######################################################################

def RecupAllMessagesNonLabelises(service):
    """
    Récupère tous les mails situés dans INBOX et les retournent dans une variable
    """
    
    label_id_one = 'INBOX'

    print("On récupère tous les messages dans la boite de réception")
    user_id =  'me'

    # On récupère tous les messages
    response = service.users().messages().list(userId='me',labelIds=[label_id_one]).execute()
    messages = []
    if 'messages' in response:
      messages.extend(response['messages'])

    while 'nextPageToken' in response:
      page_token = response['nextPageToken']
      response = service.users().messages().list(userId='me', pageToken=page_token).execute()
      messages.extend(response['messages'])
      
    print("Nombre total de mail: ",len(messages))
    return messages


def MessagesNonLabelises(service):
    """
    Parcourt tous les messages dans INBOX, extrait toutes les infos et  retournent une liste final
    """
    user_id = 'me'
    messages = RecupAllMessagesNonLabelises(service = service)
    final_list = [ ]

    i=0
    for mssg in messages:
        print("Extraction info message ",i)
        i+=1
        message = service.users().messages().get(userId=user_id, id=mssg['id']).execute()
        temp_dict = ExtraitInfoMsg(service=service,message=message)
        final_list.append(temp_dict)

    return final_list





