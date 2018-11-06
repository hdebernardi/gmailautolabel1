# -*- coding: utf-8 -*-

import os
import configparser

import data.connection
import data.mail
import ml.unsupervised

# read configuration variables from config.ini file
config = configparser.ConfigParser()
config.read('./mailautolabel/data/config.ini')
hostname = config.get('account_0', 'hostname')
username = config.get('account_0', 'username')
password = config.get('account_0', 'password')

def show_messages(messages):
	for message in messages:
		print('-'*80)
		for k, v in message.items():
			print('{:30} : {}'.format(k, v))

def apply_ml(messages):
	data={'text': []}
	
	for message in messages:
		data['text'].append(message['Body'])
	

	print('-'*80)
	print('ML UNSUPERVISED TO TRY LIBRARIES')
	print('-'*80)
	ml.unsupervised.get_scores(data)

# context manager ensures the session is cleaned up
with data.connection.open(hostname, username, password, verbose=True) as c:
	messages = data.mail.get_messages(c, verbose=True)
	parsed_messages = data.mail.get_useful_parts_of_messages(messages)

	show_messages(parsed_messages)
	apply_ml(parsed_messages)