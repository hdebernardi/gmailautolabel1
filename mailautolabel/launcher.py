# -*- coding: utf-8 -*-

import csv

import imap.connection
import imap.mail
import ml.unsupervised
import csv_helper
import sys

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
def enterMail():
	method=input("Entrez 0 pour utiliser une adresse par défaut"
              "\n       1 pour entrer votre propre adresse mail"
	      "\nSaisir: ")


	# read configuration variables from config.ini file
	if method == "0":
		hostname = 'imap.gmail.com'
		username = 'm1.autolabel1@gmail.com'
		password = 'm1-luminy'
	#user enter variables
	elif method == "1":
		hostname = input("Entrez l'adresse imap : ")
		username = input("Entrez l'adresse email : ")
		password = input("Entrez votre mot de passe : ")
	else:
		print("Saisi incorrect")
		sys.exit(0)
	
	return (hostname,username,password)

######################################################################
def main():
	print("----------------GMAIL AUTOLABEL 1----------------------")
	connect=enterMail()
	hostname = connect[0]
	username = connect[1]
	password = connect[2]

	firstCo( hostname=hostname, username=username, password=password)
	
	'''A FINIR DE COMPLETER QUAND ON AURA TOUTES LES FONCTIONS NECESSAIRE
	#If file csv exist
	if csv_helper.is_present(username=username) == 1:
		print("Il y a déjà un fichier csv de créer")
		print("0: labéliser les mails 1: réentrainer le modèle")
		method = input("Saisir:")
		if method == "0":
			print("ok")
			#labél mails
		if method == "1":
			print("ok")
			#train the model
	#If file csv doesn't exist
	else:
		print("Le fichier csv n'a pas encore était crée")
		firstCo( hostname=hostname, username=username, password=password)'''

	
if __name__ == '__main__':
   main()
