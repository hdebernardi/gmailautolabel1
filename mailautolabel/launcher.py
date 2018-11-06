# -*- coding: utf-8 -*-

import os
import configparser
import csv

import imap.connection
import imap.mail
import ml.unsupervised

# read configuration variables from config.ini file
config = configparser.ConfigParser()
config.read('./mailautolabel/imap/config.ini')
hostname = config.get('account_0', 'hostname')
username = config.get('account_0', 'username')
password = config.get('account_0', 'password')

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
def save_mails_csv(username, mails):
	filename = 'data/{}.csv'.format(username)

	try:
		file = open(filename, 'r')
	except IOError:
		file = open(filename, 'w')
	
	keys = mails[0].keys()
	with open(filename, 'w') as csvfile:
		writer = csv.DictWriter(csvfile, keys)
		writer.writeheader()
		writer.writerows(mails)

################################################################################
# context manager ensures the session is cleaned up
with imap.connection.open(hostname, username, password, verbose=True) as c:
	full_mails = imap.mail.get_mails(c, verbose=True)
	mails = imap.mail.get_useful_parts_of_mails(full_mails)
	
	save_mails_csv(username, mails)
	show_mails(mails)
	apply_ml(mails)