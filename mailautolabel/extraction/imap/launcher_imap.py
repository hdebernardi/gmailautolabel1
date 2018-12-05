# -*- coding: utf-8 -*-

import csv
import sys

import extraction.imap.connection as connection
import extraction.imap.mail as mail
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

def lancementImap(hostname,username,password):
	hostname = 'imap.gmail.com'
	username = 'chucknorrism1luminy@gmail.com'
	password = 'm1luminy'
	# context manager assure que la session est nettoyée
	with connection.open(hostname, username, password, verbose=True) as c:
		full_mails = mail.getMails(c, verbose=True)
		mails = mail.getUsefulPartsOfMails(full_mails)
	
		csv_helper.saveMails(username, mails)
		showMails(mails)


