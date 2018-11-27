.. GmailAddon documentation master file, created by
   sphinx-quickstart on Mon Oct 29 09:36:13 2018.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

connection
======================================


def open(hostname, username, password, verbose=False):
	- Ouvre une connection vers une boite mail.
	- Paramètres :
		* ``hostname`` : nom du serveur auquel nous voulons nous connecter (ex : gmail, aol).
		* ``username`` : identifiant de l'utilisateur de la boite mail.
		* ``password`` : mot de passe de l'utilisateur de la boite mail.
	- Retourne la ``connexion`` avec le serveur en IMAP.
