from gmail.extraction_info_mail import *
import re

#######################################################################
#               Récupère tous les mails lablélisé, extrait les infos  #  
#                    et les stocke dans une liste                     #
#######################################################################

def recupAllMessages(service,label=None,fenetre=None):
    """
    Récupère tous les mails de la boite
    """
    
    if(label==None):    
        print("On récupère tous les messages de la boite mail")
    else:
        label['text'] = "On récupère tous les messages de la boite mail\n"
        fenetre.update()
        
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
    
    if(label==None):  
        print("Nombre total de mail: ",len(messages))
    else:
        label['text'] += "Nombre total de mail: " + str(len(messages))+ "\n"
        fenetre.update()
    return messages

def allMessage(service,label=None,fenetre=None):
    """
    Parcourt tous les messages de la boite mail.
    Si la case 'Folder' est == à False cela signifie que le mail n'est pas labélisé on ne l'ajoute donc pas à la liste final.
    On retourne la liste finale
    """
        
    user_id = 'me'
    
    if(label==None):
        messages = recupAllMessages(service=service)
    else:
    	messages = recupAllMessages(service=service,label=label,fenetre=fenetre)

    final_list = [ ]
    
    if(label==None):
    	print("On extrait les informations pour chaque mails")
    else:
    	label['text'] += "On extrait les informations pour chaque mails\n"
    	fenetre.update()
    # On parcourt chaque message
    i=0
    for mssg in messages:
        if(label==None):
        	print("Extraction des info du message ",i)
        else:
        	label['text'] += "Extraction des info du message "+ str(i) +"\n"
        	fenetre.update()
        i+=1
        message = service.users().messages().get(userId=user_id, id=mssg['id']).execute()
        temp_dict = extraitInfoMsg(service=service,message=message)

        # Si le mail n'est pas labélisé on ne l'ajoute pas 
        if(temp_dict['Folder'] == 'False'):
            pass
        # Sinon on l'ajoute
        else:
            final_list.append(temp_dict)

    return final_list

#######################################################################
#         Récupère tous les mails non labelisés, extrait les infos    #
#                et les stocke dans une liste                         #
#######################################################################

def recupAllMessagesNonLabelises(service,label=None,fenetre=None):
    """
    Récupère tous les mails situés dans INBOX et les retourne dans une variable
    """
    
    label_id_one = 'INBOX'
    
    if(label==None):
        print("On récupère tous les messages dans la boite de réception")
    else:
        label['text'] += "On récupère tous les messages dans la boite de réception\n"
        fenetre.update()
        
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
      
    if(label==None):
        print("Nombre total de mail dans la boite de reception: ",len(messages))
    else:
        label['text'] += "Nombre total de mail dans la boite de reception " + str(len(messages)) +"\n"
        fenetre.update()
        
    return messages


def messagesNonLabelises(service,label=None,fenetre=None):
    """
    Parcourt tous les messages dans INBOX, extrait toutes les infos et retourne une liste final.
    """
    user_id = 'me'
    if(label==None):
        messages = recupAllMessagesNonLabelises(service=service)
    else:
        messages = recupAllMessagesNonLabelises(service=service,label=label,fenetre=fenetre)
    final_list = [ ]

    i=0
    for mssg in messages:
        if(label==None):
        	print("Extraction des info du message ",i)
        else:
                label['text'] += "Extraction des info du message " + str(i) + "\n"
                fenetre.update()
        i+=1
        message = service.users().messages().get(userId=user_id, id=mssg['id']).execute()
        temp_dict = extraitInfoMsg(service=service,message=message)
        final_list.append(temp_dict)

    return final_list





