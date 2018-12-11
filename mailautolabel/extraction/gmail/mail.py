import re
from graphics.affichage_graphique import affiche
import dateutil.parser as parser
import base64
from bs4 import BeautifulSoup
import re
import sys


#######################################################################
#                          Nettoie le corps du mail                   #
#######################################################################

def clearBody(part_data):
    '''  
    -Nettoie le corps du mail en le décodant depuis base64.
    -Paramètre :
        -``part_data`` : Corps du mail en base64.
    -Renvoie ``message``, le corps du text traité.
    '''   
    # decode depuis Base64 vers UTF-8
    clean_one = part_data.replace("-","+")
    # decode depuis Base64 vers UTF-8
    clean_one = clean_one.replace("_","/") 
    # decode depuis Base64 vers UTF-8
    clean_two = base64.b64decode (bytes(clean_one, 'UTF-8'))
    soup = BeautifulSoup(clean_two , "lxml" )
    message=soup.get_text()
    return message

#######################################################################
#                  Extrait les informations importantes du mail       #
#######################################################################

def extraitInfoMsg(service,message):
    '''
    -Extrait les informations utiles du message vers un dictionnaire temp_dict.
    -Paramètres:
        -``service`` : service de messagerie utilisé (ex : gmail)
        -``message`` : un mail, avec toutes ses informations.
    -Renvoie temp_dict, contenant :
        -``id``: L'identifiant du message.
        -``Label`` : Liste des labels du mail.
        -``Folder`` : Label mis par l'utilisateur (si vide = False).
        -``Subject`` : Objet du mail.
        -``Date`` : Date du mail au format YYYY-MM-DD.
        -``Sender`` : Expéditeur du mail.
        -``Snippet`` : Snippet du message.
        -``Message_body`` : Corps du message, après traitement.
    '''   
    user_id = 'me'
    temp_dict = {} 

    # RECUPERE L'ID
    temp_dict['id'] = message['id']

    # SI LE MAIL EST TRIE RECUPERE L'ID DU LABEL/FOLDER
    # on vérfie si le mail possède un label de la forme "Label_*"
    # si c'est le cas, cela veut dire que le mail a été trié par l'utilisateur et qu'il se situe dans le folder.
    expression = r"Label_*"
    for label in message['labelIds']:
        if re.search(expression, label) is not None:
            temp_dict['Folder'] = label

    payld = message['payload'] # récupère le payload du message
    headr = payld['headers'] # récupère le header du payload

    for each in headr:
        #recup le nom
        if each['name'] == 'Subject':
            temp_dict['Subject']  = each['value']

        #recup la date
        if each['name'] == 'Date':
            date_parse = (parser.parse(each['value']))
            temp_dict['Date'] = str(date_parse.date())

        #recup l'expéditeur
        if each['name'] == 'From':
            temp_dict['Sender'] = each['value']


    # RECUPERE LE SNIPPET
    temp_dict['Snippet'] = message['snippet']
    
    # RECUPERE LE CORPS
    try:
        mssg_parts = payld['parts'] # récupération des parties du message
        part_one  = mssg_parts[0] # récupération du premier élément des parties
        part_body = part_one['body'] # récupération du corps du message
        if part_body['size']==0:
           mssg_body =' '
        else: 
            part_data = part_body['data'] # récupération des données du corps
            # on récupère le body au bon format 
            mssg_body = clearBody(part_data=part_data)
        temp_dict['Message_body'] = mssg_body
    except :
        pass

    return temp_dict


#######################################################################
#               Récupère tous les mails lablélisé, extrait les infos  #  
#                    et les stocke dans une liste                     #
#######################################################################

def recupAllMessages(service,type_extraction):
    """
    -Récupère tous les mails de la boite
    -Paramètres :
        -``service`` : service de messagerie utilisé (ex : gmail)
        -``type_extraction`` : si == "NON_LABEL", renvoie les mails non labélisés, tout sinon.
    -Renvoie ``messages``, la liste des mails.
    """
    user_id = 'me'

    # On récupère tous les messages
    if(type_extraction == "NON_LABEL"):
        response = service.users().messages().list(userId='me',labelIds=['INBOX']).execute()
    else:
        response = service.users().messages().list(userId='me').execute()
  
    messages = []
    if 'messages' in response:
      messages.extend(response['messages'])

    while 'nextPageToken' in response:
      page_token = response['nextPageToken']
      if(type_extraction == "NON_LABEL"):
          response = service.users().messages().list(userId='me',labelIds=['INBOX'],pageToken=page_token).execute()
      else:
          response = service.users().messages().list(userId='me',pageToken=page_token).execute()
      messages.extend(response['messages'])

    return messages


def allMessage(service,type_extraction,label=None,fenetre=None):
    """
    -   Parcourt tous les messages de la boite mail.
        Si la case 'Folder' est == à False cela signifie que le mail n'est pas labélisé on ne l'ajoute donc pas à la liste final.
        On retourne la liste finale
    - Paramètres :
        -``service`` : service de messagerie utilisé (ex : gmail)
        -``type_extraction`` : si == "NON_LABEL", renvoie les mails non labélisés, tout sinon.
        -``label`` : Zone de text de destination si en mode graphique, inexistant sinon.
        -``fenetre`` : Fenetre de destination pour affichage si en mode graphique, inexistante sinon.
    -Retourne ``final_list``, liste de tout les mails traitée.
    """

    user_id = 'me'
    if(type_extraction == "NON_LABEL"):
        affiche("On récupère tous les mails non labélisés\n",0,label ,fenetre)
        messages=recupAllMessages(service,"NON_LABEL")
    else:
        affiche("On récupère tous les mails\n",0,label ,fenetre)
        messages=recupAllMessages(service,"TOUT")

    affiche("Nombre total de mail: "+str(len(messages))+"\n",1,label ,fenetre)
    final_list = [ ]

    affiche("On extrait les informations pour chaque mails\n",1,label ,fenetre)
    # On parcourt chaque message
    i=0
    for mssg in messages:
        affiche(str(i)+"/"+str(len(messages))+"\n" ,1,label ,fenetre)
        i+=1
        message = service.users().messages().get(userId=user_id, id=mssg['id']).execute()
        temp_dict = extraitInfoMsg(service=service,message=message)
        final_list.append(temp_dict)

    return final_list
