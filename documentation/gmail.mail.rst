..GmailAddon documentation master file, created by
   sphinx-quickstart on Mon Oct 29 09:36:13 2018.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

gmail.mail.rst
======================================
**Traite les mails en utilisant IMAP**

def clearBody(part_data):
    - Nettoie le corps du mail en le décodant depuis base64.
    - Paramètre :
        -``part_data`` : Corps du mail en base64.
    - Renvoie ``message``, le corps du text traité.

def extraitInfoMsg(service,message):
    -Extrait les informations utiles du message vers un dictionnaire temp_dict.
    -Paramètres:
        -``service`` : servic
    -Renvoie temp_dict, contenant :
        -``id``: L'identifiant du message.
        -``Label`` : Liste des labels du mail.
        -``Folder`` : Label mis par l'utilisateur (si vide = False).
        -``Subject`` : Objet du mail.
        -``Date`` : Date du mail au format YYYY-MM-DD.
        -``Sender`` : Expéditeur du mail.
        -``Snippet`` : Snippet du message.
        -``Message_body`` : Corps du message, après traitement.
	
def recupAllMessages(service,type_extraction):
    -Récupère tous les mails de la boite
    -Paramètres :
        -``service`` : service de messagerie utilisé (ex : gmail)
        -``type_extraction`` : si == "NON_LABEL", renvoie les mails non labélisés, tout sinon.
    -Renvoie ``messages``, la liste des mails.
    
def allMessage(service,type_extraction,label=None,fenetre=None):
    -   Parcourt tous les messages de la boite mail.
        Si la case 'Folder' est == à False cela signifie que le mail n'est pas labélisé on ne l'ajoute donc pas à la liste final.
        On retourne la liste finale
    - Paramètres :
        -``service`` : service de messagerie utilisé (ex : gmail)
        -``type_extraction`` : si == "NON_LABEL", renvoie les mails non labélisés, tout sinon.
        -``label`` : Zone de text de destination si en mode graphique, inexistant sinon.
        -``fenetre`` : Fenetre de destination pour affichage si en mode graphique, inexistante sinon.
    -Retourne ``final_list``, liste de tout les mails traitée.
    
 
