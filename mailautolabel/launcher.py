# -*- coding: utf-8 -*-

import csv

import imap.connection
import imap.mail
import ml.unsupervised
import csv_helper
import sys
from graphics.InterfaceGraphique import AffichageTexteSimple

################################################################################
def show_mails(mails):
	for mail in mails:
		print('-'*80)
		for k, v in mail.items():
			print('{:30} : {}'.format(k, v))


##########################################################################

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

def firstCo(hostname,username,password):
	# context manager ensures the session is cleaned up
	with imap.connection.open(hostname, username, password, verbose=True) as c:
		full_mails = imap.mail.get_mails(c, verbose=True)
		mails = imap.mail.get_useful_parts_of_mails(full_mails)
	
		csv_helper.save_mails(username, mails)
		show_mails(mails)
		#apply_ml(mails)

###################################################################
#return hostname,username,password by default or cho
def argMail(flag_mail):
	# read configuration variables from config.ini file
	if flag_mail == False:
		hostname = 'imap.gmail.com'
		username = 'm1.autolabel1@gmail.com'
		password = 'm1-luminy'
	#user enter variables
	elif flag_mail == True:
		hostname = input("Enter imap adress : ")
		username = input("Enter mail : ")
		password = input("Enter password : ")
	
	return (hostname,username,password)

######################################################################
def main():
	print("----------------GMAIL AUTOLABEL 1----------------------")

	flag_graphics = False
	flag_mail = False
	for arg in sys.argv:
		if arg == "-graphics":
			flag_graphics = True
		elif arg == "-mail":
			flag_mail = True	
 
	############################## Argument -graphics
	if flag_graphics == True:
		AffichageTexteSimple("L'affichage de texte fonctionne bien.\n"
					" Il suffit d'appeler la fonction avec texte.\n"
					" Texte etant ce qu'on veux afficher.")

	############################## Argument -mail
	connect = argMail(flag_mail = flag_mail)
	#On récupère hostname, username,password
	hostname = connect[0]
	username = connect[1]
	password = connect[2]

	firstCo( hostname=hostname, username=username, password=password)

	
if __name__ == '__main__':
   main()
