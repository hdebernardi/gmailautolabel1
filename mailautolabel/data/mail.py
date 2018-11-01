# -*- coding: <utf-8> -*-

import email
import chardet

################################################################################
def get_header(mail, keys=['Date', 'From', 'To', 'Subject']):
	dict_to_return = {}
	
	for key in keys:
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

	for part in mail.walk():
		# as for now, we only get text/plain part
		# we should deal with text/html data and attachments later
		if part.get_content_type() == 'text/plain':
			str_body = part.get_payload(decode=True)
			if(str_body):
				encoding = chardet.detect(str_body)['encoding']
				str_body = str_body.decode(encoding, errors='ignore')
				dict_to_return['Body'] = str_body

		if(not 'Body' in dict_to_return or dict_to_return['Body'] == ''):
			dict_to_return['Body'] = 'RIEN DU TOUT, FAUT TRAITER'

		dict_to_return['Content-type'].append(part.get_content_type())

	return dict_to_return

################################################################################
def get_folders(connection, verbose=False):
	if(verbose):
		print('Getting folders...')
		
	folders = []
	raw_folders = connection.list_folders()
	for raw_folder in raw_folders:
		folders.append(raw_folder[-1])
	
	if(verbose):
		print(folders)
	
	return folders

################################################################################
def get_messages(connection, verbose=False):
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
			full_message['ID'] = message_id
			full_message['Folder'] = folder
			full_message.update(get_flags(flags))
			full_message.update(get_header(mail))
			full_message.update(get_body(mail))

			all_messages.append(full_message)

	return all_messages
