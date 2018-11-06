from __future__ import print_function
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
import email
from apiclient import errors
import dateutil.parser as parser
import base64
from bs4 import BeautifulSoup

#######################################################################
#   Affiche le contenu de tous les mails present sur la boite gmail   #
#######################################################################
def AllMessage(GMAIL):
    user_id =  'me'

    # Getting all messages from Inbox
    msgs = GMAIL.users().messages().list(userId='me').execute()
    # We get a dictonary. Now reading values for the key 'messages'
    mssg_list = msgs['messages']

    final_list = [ ]

    for mssg in mssg_list:
        temp_dict = {}
        m_id = mssg['id'] # get id of individual message
        message = GMAIL.users().messages().get(userId=user_id, id=m_id).execute() # fetch the message using API
        payld = message['payload'] # get payload of the message 
        headr = payld['headers'] # get header of the payload

        for one in headr: # getting the Subject
            if one['name'] == 'Subject':
                msg_subject = one['value']
                temp_dict['Subject'] = msg_subject
            else:
                pass

        for two in headr: # getting the date
            if two['name'] == 'Date':
                msg_date = two['value']
                date_parse = (parser.parse(msg_date))
                m_date = (date_parse.date())
                temp_dict['Date'] = str(m_date)
            else:
                pass

        for three in headr: # getting the Sender
            if three['name'] == 'From':
                msg_from = three['value']
                temp_dict['Sender'] = msg_from
            else:
                pass

        #temp_dict['Snippet'] = message['snippet'] # fetching message snippet
    
        try:
            # Fetching message body
            mssg_parts = payld['parts'] # fetching the message parts
            part_one  = mssg_parts[0] # fetching first element of the part 
            part_body = part_one['body'] # fetching body of the message
            part_data = part_body['data'] # fetching data from the body
            # decoding from Base64 to UTF-8
            clean_one = part_data.replace("-","+")
            # decoding from Base64 to UTF-8
            clean_one = clean_one.replace("_","/") 
            # decoding from Base64 to UTF-8
            clean_two = base64.b64decode (bytes(clean_one, 'UTF-8'))
            soup = BeautifulSoup(clean_two , "lxml" )
            mssg_body = soup.body()
            # mssg_body is a readible form of message body
            # depending on the end user's requirements, it can be further cleaned 
            # using regex, beautiful soup, or any other method
            temp_dict['body'] = mssg_body
        except :
            pass
 
        final_list.append(temp_dict) # This will create a dictonary item in the final list
    return final_list

if __name__ == '__main__':
	store = file.Storage('token.json')
	creds = store.get()
	if not creds or creds.invalid:
		flow = client.flow_from_clientsecrets('credentials.json', SCOPES)
		creds = tools.run_flow(flow, store)
	service = build('gmail', 'v1', http=creds.authorize(Http()))

	messages = AllMessage(service)
	
	for msg in messages:
		print('-'*80)
		for k, v in msg.items():
			print('{:20} : {}'.format(k, v))
