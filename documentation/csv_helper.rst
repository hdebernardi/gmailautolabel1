.. GmailAddon documentation master file, created by
   sphinx-quickstart on Mon Oct 29 09:36:13 2018.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

csv_helper
======================================

def getPath(username):
	"""
	- Renvoie le chemin absolu du fichier "username".csv
		-   Note:
			cheminFich = 'data/{}.csv'.format(username) 
			Cela fonctionne mais probablement pas sur tout les OS
	- Paramètre :
		- ``username`` : identifiant de l'ulisateur (addresse mail).
	- Retourne ``abs_path``, le chemin absolu du fichier "username".csv.

def isPresent(username):
	- Retourne 1 si le chemin "username".csv est présent, 0 sinon
	- Paramètre :
		- ``username`` : identifiant de l'ulisateur (addresse mail).

def toDict(username):
	- Retourne un dictionnaire depuis un fichier csv
	- Paramètre :
		- ``username`` : identifiant de l'ulisateur (addresse mail).

def saveMails(username, mails):
	- Créer un fichier csv depuis un dictionnaire
	- Paramètres :
		- ``username`` : identifiant de l'ulisateur (addresse mail).
		- ``mails`` : liste des mails de la boite de l'utilisateur.