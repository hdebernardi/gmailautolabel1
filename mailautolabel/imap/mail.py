# -*- coding: <utf-8> -*-

import email
import chardet
import bs4

################################################################################
def decode_html(html):
	soup = bs4.BeautifulSoup(html, 'html.parser')
	
	# kill all script and style elements
	for script in soup(['script', 'style']):
		script.extract() # rip it out

	# get text
	text = soup.get_text()

	# break into lines and remove leading and trailing space on each
	lines = (line.strip() for line in text.splitlines())

	# break multi-headlines into a line each
	chunks = (phrase.strip() for line in lines for phrase in line.split(' '))
	# drop blank lines
	#text = '\n'.join(chunk for chunk in chunks if chunk)
	text = ' '.join(chunk for chunk in chunks if chunk)

	return text

################################################################################
def get_header(mail):
	dict_to_return = {}
	
	for key in mail.keys():
		if(mail[key]):
			decoded_header = email.header.decode_header(mail[key])
			header = email.header.make_header(decoded_header)
			dict_to_return[key] = str(header)

	return dict_to_return

################################################################################
def get_flags(mail):
	dict_to_return = {'Flags': []}

	for flag in mail:
		dict_to_return['Flags'].append(flag.decode().strip('\\'))

	return dict_to_return

################################################################################
def get_body(mail):
	dict_to_return = {'Content-type': []}

	has_a_text_part = 0

	for part in mail.walk():
		# as for now, we only get text/plain part
		# we should deal with text/html data and attachments later
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
				dict_to_return['Body'] = decode_html(str_body)

		dict_to_return['Content-type'].append(part.get_content_type())

	return dict_to_return

################################################################################
def get_folders(connection, verbose=False):
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
def get_mails(connection, verbose=False):
	all_messages=[]
	
	folders = get_folders(connection, verbose)

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
			full_message.update(get_flags(flags))
			full_message.update(get_header(mail))
			full_message.update(get_body(mail))

			all_messages.append(full_message)

	return all_messages


def get_useful_parts_of_mails(messages, keys=['Message-ID', 'Date', 'From', 'To', 'Subject', 'Body', 'Content-type']):
	# we should remove id tests for other mail providers than google
	all_messages = []
	ids = []

	for message in messages:
		if message['Message-ID'] not in ids:
			filtered_msg = {}
			for k, v in message.items():
				if k in message.keys():
					filtered_msg[k] = v
				
			all_messages.append(filtered_msg)
			ids.append(message['Message-ID'])
			
	return all_messages
