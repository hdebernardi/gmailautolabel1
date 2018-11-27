.. GmailAddon documentation master file, created by
   sphinx-quickstart on Mon Oct 29 09:36:13 2018.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

RecuperationMail
======================================

**Fonctions utilisant seulement le service Gmail**

def RecupAllMessages(service):
	- Récupère tout les mails d'une boite mail.
	- Paramètre :
		* ``service`` : Service utilisé pour communiquer avec la boite mail.
	- Retourne ``messages``, la iste de tout les messages.


def AllMessage(service):
	- 	Parcourt tous les messages de la boite mail.
		En extrait leurs informations.
		Si la case 'Folder' est == à False cela signifie que le mail n'est pas  labélisé on ne l'ajoute donc pas à la liste final.
	- Paramètre :
		* ``service`` : Service utilisé pour communiquer avec la boite mail.
	- Retourne ``final_list``, liste de tout les mails labelisés et traitée. 


def _RecupAllMessagesNonLabelises(service):
	- Récupère tout les messages situés dans la boite de réception INBOX de la boite mail.
	- Paramètre :
		* ``service`` : Service utilisé pour communiquer avec la boite mail.
	- Retourne ``messages`` la liste de tout les messages dans non labelisé.


def MessagesNonLabelelises(service):
	- Parcourt tous les messages dans INBOX (liste retournée par la fonction RecupAllMessagesNonLabelises(service))_ , extrait toutes les infos et retourne une liste final.
	- Paramètre :
		* ``service`` : Service utilisé pour communiquer avec la boite mail.
	- retourne ``final_list``, la liste des mails traités.
