.. GmailAddon documentation master file, created by
   sphinx-quickstart on Mon Oct 29 09:36:13 2018.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

supervised
======================================


**Ce fichier..**

def supervised_split(username):
	- Cette focntion fait...


def supervised_with_nolabelling_mail(username):
	- Fonctionnement :
		* On récupère les mails non labélisés et labélisés dans des df.
		* On fait un TF-IDF pour séparer tous les mots et affiche un "score" pour chacun.
		* On fait une régression logistique entre le body et le folder des mails déjà labélisé. Le Folder est seulement le nom d'un label.
		* Une fois le classifier créé, on l'applique sur les mails non labélisés et on retourne un dictionnaire contenant tous les labels de prédictions.
	- Paramètre :
		* ``username`` : Nomadresse email de l'utilisateur de la boite mail.
	- Retourne ``predicts``, un dictionnaire contenant tous les labels de prédictions.