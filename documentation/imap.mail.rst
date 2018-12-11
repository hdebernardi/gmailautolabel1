.. GmailAddon documentation master file, created by
   sphinx-quickstart on Mon Oct 29 09:36:13 2018.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

imap.mail
======================================
def decodeHtml(html):
    	- Decode du text au format html en un text simple sans format.
        - Paramètre :
        		* ``html`` : Un text au format html.    
        - Renvoie ``text``, le text html décodé.
        
def getHeader(mail):
        - Récupère l'entète du mail.
        - Paramètre :
        		* ``mail`` : Un mail.
        - Retourne ``dict_to_return`` contenant l'entète du mail.
        
def getFlags(mail):
	- Récupère les labels du mail.
	- Paramètre :
		* ``mail`def getBody(mail):
	- Récupère le corps du mail.
	- Paramètre :
		* ``mail`` : Un mail.
	- Retourne le dictionnaire ``dict_to_return`` contenant le corps du message.
	- Retourne le dictionnaire ``dict_to_return`` contenant la liste des labels.

def getBody(mail):
	- Récupère le corps du mail.
	- Paramètre :
		* ``mail`` : Un mail.
	- Retourne le dictionnaire ``dict_to_return`` contenant le corps du message.
	
def getFolders(connection, verbose=False):
	- Récupère les dossiers présents dans la boite mail.
	- Paramètres :
		* ``connection`` : une connection vers une boite mail.
		* ``verbose`` : permet d'afficher ce que la fonction fait (default = False).
	- Retourne ``folders``, la liste des dossiers.
	
def getMails(connection, verbose=False):
	- Récupère les mails présents dans une boite mail en utilisant les fonctions précédentes.
	- Paramètres :
		* ``connection`` : une connection vers une boite mail.
		* ``verbose`` : permet d'afficher ce que la fonction fait (default = False).
	- Retourne ``all_messages``, une liste de mails.
	
def getUsefulPartsOfMails(mails):
	- Ne récupère seulment les parties utiles des mails.
	- Paramètre :
		* ``mails`` : une liste de mails.
	- Retourne ``all_mails``, la liste des mails traitée.




	
