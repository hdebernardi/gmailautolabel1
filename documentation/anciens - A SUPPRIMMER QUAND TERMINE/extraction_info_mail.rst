.. GmailAddon documentation master file, created by
   sphinx-quickstart on Mon Oct 29 09:36:13 2018.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

ExtractionInfoMail
======================================


**Ce fichier..**


def afficheList(final_list):
	- Affiche la liste des mails dont leurs ``id`` et leur ``body``.
	- Paramètre :
		* ``final_list`` : Liste de mails.


def clearBody(part_data):
	- Nettoie le corps du mail en le décodant depuis base64.
	- Paramètre :
		* ``part_data`` : Corps du mail en base64.
	- Renvoie ``message``, le corps du text traité. 

	
def extraitInfoMsg(service,message):
	- Extrait les informations utiles du message vers un dictionnaire ``temp_dict``.
	- Paramètres :
		* ``service`` : service de messagerie utilisé (ex : gmail)
		* ``message`` : un mail, avec toutes ses informations.
	- Renvoie ``temp_dict``, contenant :
		* ``id`` : L'identifiant du message.
		* ``Label`` : Liste des labels du mail.
		* ``Folder`` : Label mis par l'utilisateur (si vide = False).
		* ``Subject`` : Objet du mail.
		* ``Date`` : Date du mail au format YYYY-MM-DD.
		* ``Sender`` : Expéditeur du mail.
		* ``Snippet`` : Snippet du message.
		* ``Message_body`` : Corps du message, après traitement.

