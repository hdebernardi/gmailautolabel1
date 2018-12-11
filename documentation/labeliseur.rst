.. GmailAddon documentation master file, created by
   sphinx-quickstart on Mon Oct 29 09:36:13 2018.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

labeliseur
======================================
def ajoutLabel(service,labelId,messageId):
    	-Pramètres :
            -``service`` : service de messagerie utilisé (ex : gmail)
            -``labelId`` : Identifiant deu label à ajouter.
            -``messageId`` : identifiantdu mail à labéliser.
            
def gmailLabelisation(service,username,label =None,fenetre = None):
