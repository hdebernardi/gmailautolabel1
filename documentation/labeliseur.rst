.. GmailAddon documentation master file, created by
   sphinx-quickstart on Mon Oct 29 09:36:13 2018.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

labeliseur
======================================
def ajoutLabel(service,labelId,messageId):
	-Ajoute le label "labelId" au mail "messageId"
	- Pramètres :
		-``service`` : service de messagerie utilisé (ex : gmail)
		-``labelId`` : Identifiant deu label à ajouter.
		-``messageId`` : identifiantdu mail à labéliser.

def gmailLabelisation(service,username,label =None,fenetre = None):
	-	Démarre le machine learning sur la boite mail de l'utilisateur,
		puis en fonction, labélise les mails non labélisés
	- Paramètres
		-``service`` : service de messagerie utilisé (ex : gmail)
		-``username`` : identifiant de l'utilisateur de la boite mail (addresse mail).
		-``label`` : Zone de text de destination si en mode graphique, inexistant sinon.
		-``fenetre`` : Fenetre de destination pour affichage si en mode graphique, inexistante sinon.
