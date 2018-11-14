import dateutil.parser as parser
import base64
from bs4 import BeautifulSoup
import re
import sys

#######################################################################
#                        Affiche la liste                             #
#######################################################################

def afficheList(final_list):
    print ("Total messaged retrived: ", str(len(final_list)))
    i = 1
    for var in final_list:
        print("--------------------------------------------message ",i)
        i += 1
        print("id ",var['id'])
        #print("Sender ",var['Sender'])
        print("Date ",var['Date'])
        print("Subject ",var['Subject'])
        #print("Snippet",var['Snippet'])
        print("Label",var['Label'])
        #print("Body ",var['Message_body'])


#######################################################################
#                          Nettoie le corps du mail                   #
#######################################################################

def clearBody(part_data):
    # decoding from Base64 to UTF-8
    clean_one = part_data.replace("-","+")
    # decoding from Base64 to UTF-8
    clean_one = clean_one.replace("_","/") 
    # decoding from Base64 to UTF-8
    clean_two = base64.b64decode (bytes(clean_one, 'UTF-8'))
    soup = BeautifulSoup(clean_two , "lxml" )
    message=soup.body()

    #on récupère l'intérieur des balises <p> </p> avec le nom des balises écrites
    '''for p in soup.find_all('p'):
       print(p)'''

    #on récupère l'intérieur des balises <p> </p> avec le nom des balises NON ecrites
    '''for p in soup.p.find_all(string=True):
    print(p)'''

    #supprime toutes les balises <htpps:> .* </https:>
    '''test = "<p> ca on <https:>ca on supprime</https:>garde</p> <https:>ici cest le deuxieme supprime</https:>"
    cleanr =  re.compile('<https:>(.*?)</https:>')
    cleantext = re.sub(cleanr, '', test)
    print(cleantext)'''

    return message

#######################################################################
#                  Extrait les informations importantes du mail       #
#######################################################################

def ExtraitInfoMsg(service,message):
    user_id = 'me'
    temp_dict = {} 

    # RECUPERE L'ID
    temp_dict['id'] = message['id']

    # RECUPERE LES LABELS
    temp_dict['Label'] = [] #on crée la clé 'Label'
    labelIds = message['labelIds']
    for labelId in labelIds:
        label = service.users().labels().get(id=labelId,userId= user_id).execute() #on récupère le label
        temp_dict['Label'].append(label['name']) #on stocke le nom du label

    payld = message['payload'] # récupère le payload du message
    headr = payld['headers'] # récupère le header du payload

    # RECUPERE LE SUJET
    for one in headr:
        if one['name'] == 'Subject':
            msg_subject = one['value']
            temp_dict['Subject'] = msg_subject
        else:
            pass

    # RECUPERE LA DATE
    for two in headr:
        if two['name'] == 'Date':
            msg_date = two['value']
            date_parse = (parser.parse(msg_date))
            m_date = (date_parse.date())
            temp_dict['Date'] = str(m_date)
        else:
            pass

    # RECUPERE L'EXPEDITEUR
    for three in headr:
        if three['name'] == 'From':
            msg_from = three['value']
            temp_dict['Sender'] = msg_from
        else:
            pass


    # RECUPERE LE SNIPPET
    temp_dict['Snippet'] = message['snippet']
    
    # RECUPERE LE CORPS
    try:
        mssg_parts = payld['parts'] # fetching the message parts
        part_one  = mssg_parts[0] # fetching first element of the part 
        part_body = part_one['body'] # fetching body of the message
        part_data = part_body['data'] # fetching data from the body
        #on récupère le body au bon format 
        mssg_body = clearBody(part_data=part_data)
        temp_dict['Message_body'] = mssg_body
    except :
        pass

    return temp_dict
    '''
    temp_dict:
    {
    'id': id of mail	
    'Sender': '"email.com" <name@email.com>', 
    'Subject': 'Lorem ipsum dolor sit ametLorem ipsum dolor sit amet', 
    'Date': 'yyyy-mm-dd', 
    'Snippet': 'Lorem ipsum dolor sit amet'
    'Message_body': 'Lorem ipsum dolor sit amet'
    'Label': [ , , ]
    }
    '''

