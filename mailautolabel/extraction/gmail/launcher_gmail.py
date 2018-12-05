import extraction.gmail.mail as mail
import extraction.gmail.connection as connection
import labelisation.labeliseur as labeliseur

from tkinter.messagebox import *
import csv_helper

#############################################################################
#On extrait tous les mails
#type_extraction = "TOUT" ou "NON_LABEL"
def extracteur(username,service,type_extraction,label=None,fenetre=None):
    """
    Créer un fichier csv pour les mails déjà labélisés et
    ceux non labélisés
    """
    test = mail.recupAllMessages(service,type_extraction)
    allMails = mail.allMessage(service,type_extraction,label,fenetre)
    labelisedMails = []
    unlabelisedMails = []
    for msg in allMails:
        if('Folder' in msg): 
            labelisedMails.append(msg)
        else:
            unlabelisedMails.append(msg)

    csv_helper.saveMails("NON_LABEL"+username,unlabelisedMails)
    if(type_extraction == "TOUT"):
        csv_helper.saveMails(username, labelisedMails)

#######################################################################
#  			 Fonction principale                          #
#######################################################################
def lancementGmail(label=None,fenetre=None):
	"""
	Ce connecte au service de Gmail.
	Si c'est la première connection de l'utilisateur, crée un fichier csv pour les mails labélisés et non labélisés.
	Si ce n'est pas la première connection, soit on réentraine le modèle, soit on appelle la fonction de ML et on labélise les mails.
	"""
	service = connection.open()

	#on récupère l'adresse mail de l'utilisateur
	profile = service.users().getProfile(userId = 'me').execute()
	username = profile['emailAddress']
	    
	#Si aucun fichier csv n'est crée pour username, c'est une première connection
	if(csv_helper.isPresent(username) == 0):
		extracteur(username,service,"TOUT",label,fenetre)
	#Sinon on propose deux choix à l'utilisateur
	else:
		choix = 2
		if(label==None):
			choix=input("Désirez-vous:\n Télécharger tous vos mails(Taper 1)\n Labéliser vos mails (Taper 2)\n Saisir:")
		else:
			if askyesno("Entrainement de l'IA", "Télécharger tous vos mails ?") == True:
				choix = "1"
			else:
				choix = "2"

		#Téléchargement des mails
		if(choix == "1"):
			extracteur(username,service,"Tout",label,fenetre)
		#Labéliser les mails
		else:
			extracteur(username,service,"NON_LABEL",label,fenetre)
			labeliseur.gmailLabelisation(service,username,label,fenetre)
