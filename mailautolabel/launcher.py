# -*- coding: utf-8 -*-

import os
import configparser

import data.connection
import data.mail
import ml.unsupervised

# read configuration variables from config.ini file
config = configparser.ConfigParser()
config.read('./mailautolabel/data/config.ini')
hostname = config.get('server', 'hostname')
username = config.get('account', 'username')
password = config.get('account', 'password')

# context manager ensures the session is cleaned up
with data.connection.open(hostname, username, password, verbose=True) as c:
	messages = data.mail.get_messages(c, verbose=True)
	
	data={'text': []}
	
	for message in messages:
		data['text'].append(message['Body'])
	
	ml.unsupervised.get_scores(data)
