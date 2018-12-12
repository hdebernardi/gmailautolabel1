# -*- coding: <utf-8> -*-

import email
import chardet
import bs4

################################################################################
def decodeHtml(html):
    '''
    - Decode du text au format html en un text simple sans format.
    - Paramètre :
        * ``html`` : Un text au format html.
    - Renvoie ``text``, le text html décodé. '''
    
    soup = bs4.BeautifulSoup(html, 'html.parser')
    
    # Détruit tous les éléments de script et de style
    for script in soup(['script', 'style']):
        script.extract() # l'enlève

    # Récupère le text
    text = soup.get_text()

    # Divise en lignes et enlève les espaces à gauche et à droite sur chacune d'elles
    lines = (line.strip() for line in text.splitlines())

    # break multi-headlines into a line each
    chunks = (phrase.strip() for line in lines for phrase in line.split(' '))
    # Rajout de ligne vide
    #text = '\n'.join(chunk for chunk in chunks if chunk)
    text = ' '.join(chunk for chunk in chunks if chunk)

    return text

################################################################################
def getHeader(mail):
    '''
    - Récupère l'entète du mail.
    - Paramètre :
        * ``mail`` : Un mail.
    - Retourne ``dict_to_return`` contenant l'entète du mail.'''
    
    dict_to_return = {}
    
    for key in mail.keys():
        if(mail[key]):
            decoded_header = email.header.decode_header(mail[key])
            header = email.header.make_header(decoded_header)
            dict_to_return[key] = str(header)

    return dict_to_return

################################################################################
def getFlags(mail):
    '''
    - Récupère les labels du mail.
    - Paramètre :
        * ``mail`` : un mail.
    - Retourne le dictionnaire ``dict_to_return`` contenant la liste des labels. '''
    
    dict_to_return = {'Flags': []}

    for flag in mail:
        dict_to_return['Flags'].append(flag.decode().strip('\\'))

    return dict_to_return

################################################################################
def getBody(mail):
    '''
    - Récupère le corps du mail.
    - Paramètre :
        * ``mail`` : Un mail.
    - Retourne le dictionnaire ``dict_to_return`` contenant le corps du message.'''
    
    dict_to_return = {'Content-type': []}

    has_a_text_part = 0

    for part in mail.walk():
        # Quant à maintenant, nous obtenons seulement `part` en text/plain
        # Nous traiterons `data` et `attachemnts` en text/html plus tard
        if part.get_content_type() == 'text/plain':
            str_body = part.get_payload(decode=True)
            if(str_body):
                encoding = chardet.detect(str_body)['encoding']
                str_body = str_body.decode(encoding, errors='ignore')
                dict_to_return['Body'] = str_body
                has_a_text_part = 1

        elif part.get_content_type() == 'text/html' and not has_a_text_part:
            str_body = part.get_payload(decode=True)
            if(str_body):
                encoding = chardet.detect(str_body)['encoding']
                str_body = str_body.decode(encoding, errors='ignore')
                dict_to_return['Body'] = decodeHtml(str_body)

        dict_to_return['Content-type'].append(part.get_content_type())

    return dict_to_return

################################################################################
def getFolders(connection, verbose=False):
    '''
    - Récupère les dossiers présents dans la boite mail.
    - Paramètres :
        * ``connection`` : une connection vers une boite mail.
        * ``verbose`` : permet d'afficher ce que la fonction fait (default = False).
    - Retourne ``folders``, la liste des dossiers.
    '''
    if(verbose):
        print('Getting folders...')
        
    folders = []
    raw_folders = connection.list_folders()
    for raw_folder in raw_folders:
        if '[Gmail]' not in raw_folder[-1]: # guard for gmail
            folders.append(raw_folder[-1])
    
    if(verbose):
        print(folders)
    
    return folders

################################################################################
def getMails(connection, verbose=False):
    '''
    - Récupère les mails présents dans une boite mail en utilisant les fonctions précédentes.
    - Paramètres :
        * ``connection`` : une connection vers une boite mail.
        * ``verbose`` : permet d'afficher ce que la fonction fait (default = False).
    - Retourne ``all_messages``, une liste de mails.
    '''
    all_messages=[]
    
    folders = getFolders(connection, verbose)

    # on recherche des messages dans tous les dossiers
    for folder in folders:
        if(verbose):
            print('Selecting folder', folder)

        connection.select_folder(folder)
        response = connection.search()
        # on récupère toutes les infos au format RFC822 et les labels
        messages = connection.fetch(response, ['RFC822', 'FLAGS'])
        # BODY.PEEK[HEADER.FIELDS (DATE FROM TO SUBJECT)] BODY.PEEK[TEXT]

        if(verbose):
            print('Fetched {} messages'.format(len(messages)))

        # toute la réponse
        for message_id, message in messages.items():
            flags = message[b'FLAGS']
            mail = email.message_from_bytes(message[b'RFC822'])

            full_message = {}
            #full_message['ID'] = message_id
            full_message['Folder'] = folder
            full_message.update(getFlags(flags))
            full_message.update(getHeader(mail))
            full_message.update(getBody(mail))

            all_messages.append(full_message)

    return all_messages

################################################################################
def getUsefulPartsOfMails(mails):
    ''' 
    - Ne récupère seulment les parties utiles des mails.
    - Paramètre :
        * ``mails`` : une liste de mails.
    - Retourne ``all_mails``, la liste des mails traitée.
    '''
    all_mails = []

    data = [[k,v] for mail in mails for k, v in mail.items()] 

    keys = [data_[0] for data_ in data]
    keys = sorted(list(set(keys)))

    for mail in mails:
        mail_obj = {}
        for key in keys:
            mail_obj[key] = mail.get(key, None)
                
        all_mails.append(mail_obj)
            
    return all_mails
