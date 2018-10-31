import os
import configparser

import data.connection
import data.mail
import ml

# read configuration variables from config.ini file
config = configparser.ConfigParser()
config.read('./mailautolabel/data/config.ini')
hostname = config.get('server', 'hostname')
username = config.get('account', 'username')
password = config.get('account', 'password')

# context manager ensures the session is cleaned up
with data.connection.open(hostname, username, password, verbose=True) as c:
	messages = data.mail.get_messages(c, verbose=True)

	# just print to check
	for message in messages:
		for key, value in message.items():
			print('{:30} : {}'.format(key, value))
