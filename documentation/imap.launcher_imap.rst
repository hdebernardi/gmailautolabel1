.. GmailAddon documentation master file, created by
   sphinx-quickstart on Mon Oct 29 09:36:13 2018.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

imap.launcher_imap
======================================

def showMails(mails):
	-Affiche la liste des mails.
	-Paramètre:
		-``mails`` : la liste de mails.
	
def lancementImap(hostname,username,password):
	-Lance la connexion en IMAP et affiche les mails récupérés.
	-Paramètres:
		-``hostname`` : nom du serveur.
		-``username`` : identifiant de l'utilisateur (addresse mail).
        -``password`` : mot de passe de l'utilisateur.
