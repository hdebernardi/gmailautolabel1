from gmail.ExtractionInfoMail import *

#######################################################################
#          Récupère tous les messages de la boite mail                #
#######################################################################
def RecupAllMessages(service):
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

#######################################################################
#               Récupère tous les mails, extrait les infos et         #
#                     les stockent dans une liste                     #
#######################################################################
def AllMessage(service):
    
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
        # On ajoute le nouvel élément du dictionnaire dans la liste final
        final_list.append(temp_dict) 

    return final_list



#######################################################################
#         Récupère tous les mails non labelisés, extrait les infos    #
#             et les stockent dans une liste                          #
#######################################################################

'''Quand on crée un label sur gmail son id est de la forme : "Label_*"
Ainsi pour savoir si un mail est déjà labélisé on vérifie si un label
de la forme "Label_*" lui est associé.'''
def MessagesNonLabelelises(service):
    user_id = 'me'
    messages = RecupAllMessages(service = service)

    final_list = [ ]
    
    suivant = 0 #passe à 1 si le mail est déjà labélisé
    # On parcourt chaque message
    for mssg in messages:
        message = service.users().messages().get(userId=user_id, id=mssg['id']).execute()
        # On vérifie si le mail est labélisé ou non
        expression = r"Label_*"
        for label in message['labelIds']:
            if re.search(expression, label) is not None:
                suivant = 1
         
        #si le mail n'est pas labélisé on l'ajoute à la list final
        if(suivant == 0):
            temp_dict = ExtraitInfoMsg(service=service,message=message)
            final_list.append(temp_dict)
        suivant = 0

    return final_list






