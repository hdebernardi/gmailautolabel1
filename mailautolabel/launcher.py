# -*- coding: utf-8 -*-

import configparser

import imap.connection
import imap.mail
import ml.unsupervised
import csv_helper

################################################################################
def show_mails(mails):
	for mail in mails:
		print('-'*80)
		for k, v in mail.items():
			print('{:30} : {}'.format(k, v))

################################################################################
def apply_ml(mails):
	data={'text': []}
	
	for mail in mails:
		data['text'].append(mail['Body'])

	print('-'*80)
	print('ML UNSUPERVISED TO TRY LIBRARIES')
	print('-'*80)
	ml.unsupervised.get_scores(data)

################################################################################
# read configuration variables from config.ini file
config = configparser.ConfigParser()
config.read('./mailautolabel/imap/config.ini')
hostname = config.get('account_0', 'hostname')
username = config.get('account_0', 'username')
password = config.get('account_0', 'password')

# context manager ensures the session is cleaned up
with imap.connection.open(hostname, username, password, verbose=True) as c:
	full_mails = imap.mail.get_mails(c, verbose=True)
	mails = imap.mail.get_useful_parts_of_mails(full_mails)

	csv_helper.save_mails(username, mails)
	#show_mails(mails)
	apply_ml(mails)
