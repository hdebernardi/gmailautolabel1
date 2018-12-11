.. GmailAddon documentation master file, created by
   sphinx-quickstart on Mon Oct 29 09:36:13 2018.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

gmail.launcher_gmail
======================================
def extracteur(username,service,type_extraction,label=None,fenetre=None):
    Créer un fichier csv pour les mails déjà labélisés et
    	-Paramètres :
    		-``username`` : identifiant de l'utilisateur (addresse mail).
            	-Paramètres :
                		-``username`` : identifiant de l'utilisateur (addresse mail).
                        -``service`` : la connection avec la boite Gmail.
                		-``type_extraction`` : si == "NON_LABEL", renvoie les mails non labélisés, tout sinon.
                        -``label`` : Zone de text de destination si en mode graphique, inexistant sinon.
                        -``fenetre`` : Fenetre de destination pour affichage si en mode graphique, inexistante sinon.
                - Retourne un tuple :
                		-``labelisedMails`` : la liste des mails labélisés.
                		-``unlabelisedMails`` : la liste des mails non-labélisés.
