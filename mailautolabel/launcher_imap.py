# -*- coding: utf-8 -*-

import csv
import sys

import imap.connection
import imap.mail
import csv_helper
import ml

################################################################################
def showMails(mails):
	for mail in mails:
		print('-'*80)
		for k, v in mail.items():
			print('{:30} : {}'.format(k, v))


##########################################################################

################################################################################
def applyMl(mails):
	data={'text': []}
	
	for mail in mails:
		data['text'].append(mail['Body'])
	

	print('-'*80)
	print('ML UNSUPERVISED TO TRY LIBRARIES')
	print('-'*80)
	ml.unsupervised.get_scores(data)

################################################################################

def connectImap(hostname,username,password):
	# context manager assure que la session est nettoyée
	with imap.connection.open(hostname, username, password, verbose=True) as c:
		full_mails = imap.mail.getMails(c, verbose=True)
		mails = imap.mail.getUsefulPartsOfMails(full_mails)
	
		csv_helper.saveMails(username, mails)
		showMails(mails)


