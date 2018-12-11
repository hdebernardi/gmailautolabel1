# -*- coding: <utf-8> -*-

import imapclient

################################################################################
def open(hostname, username, password, verbose=False):
	'''
	-Ouvre une connection vers une boite mail.
	-Paramètres :
		-hostname : nom du serveur auquel nous voulons nous connecter (ex : gmail, aol).
		-username : identifiant de l'utilisateur de la boite mail.
		-password : mot de passe de l'utilisateur de la boite mail.
	-Retourne la connexion avec le serveur en IMAP. 
	'''
	# Connexion au serveur
	if verbose :
		print('Connexion à', hostname)
	connection = imapclient.IMAPClient(host=hostname)

	# Connexion à notre compte
	if verbose:
		print('Connexion en tant que', username)
	try:
		connection.login(username, password)
		print('Connecté avec succès')
	except Exception as err:
		print('ERREUR:', err)

	return connection
