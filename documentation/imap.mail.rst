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
		* ``mail`
