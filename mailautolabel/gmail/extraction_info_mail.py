import dateutil.parser as parser
import base64
from bs4 import BeautifulSoup
import re
import sys

#######################################################################
#                        Affiche la liste                             #
#######################################################################

def afficheList(final_list):
    print ("Total de massage récupérés: ", str(len(final_list)))
    i = 1
    for var in final_list:
        print("--------------------------------------------message ",i)
        i += 1
        print("id ",var['id'])
        #print("Sender ",var['Sender'])
        #print("Date ",var['Date'])
        #print("Subject ",var['Subject'])
        #print("Snippet",var['Snippet'])
        #print("Label",var['Label'])
        print("Body ",var['Message_body'])


#######################################################################
#                          Nettoie le corps du mail                   #
#######################################################################

def clearBody(part_data):
    # decode depuis Base64 vers UTF-8
    clean_one = part_data.replace("-","+")
    # decode depuis Base64 vers UTF-8
    clean_one = clean_one.replace("_","/") 
    # decode depuis Base64 vers UTF-8
    clean_two = base64.b64decode (bytes(clean_one, 'UTF-8'))
    soup = BeautifulSoup(clean_two , "lxml" )
    #message=soup.body()
    message=soup.get_text()
    return message

#######################################################################
#                  Extrait les informations importantes du mail       #
#######################################################################

def extraitInfoMsg(service,message):
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
