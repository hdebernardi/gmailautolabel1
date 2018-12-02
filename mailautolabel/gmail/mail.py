import dateutil.parser, base64, sys, bs4, re

def ajoutLabel(service, labelId, messageId):
	"""
	Ajoute le label "labelId" au mail "messageId"
	"""
	return service.users().messages().modify(
        userId='me',
        id=messageId,
        body={'addLabelIds': [labelId]}).execute()

def clearBody(body):
    body = body.replace("-", "+")
    body = body.replace("_", "/")
    # decode depuis Base64 vers UTF-8
    body = base64.b64decode(bytes(body, 'UTF-8'))
    
    soup = bs4.BeautifulSoup(body, "html.parser")
    message = soup.get_text()
    return message

def extraitInfoMsg(message):
    extracted_message = {}
    extracted_message['id'] = message['id']
    extracted_message['threadId'] = message['threadId']
    extracted_message['snippet'] = message['snippet']
    extracted_message['historyId'] = message['historyId']
    extracted_message['internalDate'] = message['internalDate']
    extracted_message['sizeEstimate'] = message['sizeEstimate']

    # traitement du payload et headers
    payload = message['payload']
    header = payload['headers']

    for each in header:
        if each['name'] == 'Subject':
            extracted_message['subject'] = each['value']
        
        if each['name'] == 'Date':
            parsed_date = dateutil.parser.parse(each['value'])
            extracted_message['date'] = parsed_date.date()
        
        if each['name'] == 'From':
            extracted_message['from'] = each['value']
        
        try:
            extracted_message['subject']
            extracted_message['date']
            extracted_message['from']
            break
        except Exception:
            continue

    try:
        encoded_mail = payload['parts'][0]['body']['data']
        body = clearBody(encoded_mail)
        extracted_message['body'] = body
    except Exception:
        #print(err)
        #sys.exit(2)
        pass
    
    # traitement des labels
    expression = r'Label_*'
    for label in message['labelIds']:
        if re.search(expression, label) is not None:
            extracted_message['folder'] = label
            break

    return extracted_message


def getIds(service):
    # Récupère tous les mails de la boite
    # On récupère tous les messages
    response = service.users().messages().list(userId='me').execute()
    messages = []
    if 'messages' in response:
      messages.extend(response['messages'])

    while 'nextPageToken' in response:
      page_token = response['nextPageToken']
      response = service.users().messages().list(
          userId='me', pageToken=page_token).execute()
      messages.extend(response['messages'])
    
    return messages

def getMails(service):
    mails = []

    ids = getIds(service)

    for id in ids:
        mail = service.users().messages().get(
            userId='me', id=id['id']).execute()
        
        mails.append(extraitInfoMsg(mail))
    
    return mails

"""
class GmailHelper(object):
    def _parseMessageHeaders(self, message_headers):
        headers = {}

        for header in message_headers:
            if header['name'] == 'Subject':
                headers['subject'] = header['value']
            
            if header['name'] == 'Date':
                parsed_date = dateutil.parser.parse(header['value'])
                headers['date'] = parsed_date.isoformat()
            
            if header['name'] == 'From':
                headers['from'] = header['value']
            
            try:
                headers['from']
                headers['date']
                headers['subject']
                break
            except KeyError as err:
                continue
        
        return headers
    
    def _getMessageHeaders(self, message):
        return message['headers']
    
    def _getMessagePayload(self, message):
        return message['payload']
    
    def _getMessageBody(self, message_payload):
        try:
            encoded = message_payload['parts'][0]['body']['data']
            encoding = chardet.detect(encoded)['encoding']
            print(encoding)
            sys.exit(0)
            return encoded.decode(encoding, errors='ignore')
        except Exception as err:
            print(err)
            sys.exit(2)


class GmailExtractor(GmailHelper):
    def __init__(self):
        self.verbose = True
        self.service = gmail.connection.open(self.verbose)

    def _listMessages(self, labels=[]):
        rv = self.service.users().messages().list(
            userId='me', labelIds=labels).execute()
        
        return rv.get('messages', [])

    def _getMessage(self, message_id):
        return self.service.users().messages().get(
            userId='me', id=message_id).execute()

    def _getLabels(self):
        rv = self.service.users().labels().list(
            userId='me').execute()
        labels = rv.get('labels', [])
        return [label['id'] for label in labels if 'messageListVisibility' not in label]
    
    def getMessages(self):
        messages = []

        rv = self._listMessages()

        for msg in rv:
            messages.append(extraitInfoMsg(msg))

        return messages
"""