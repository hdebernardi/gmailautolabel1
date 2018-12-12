import ml.supervised
import csv_helper
from  graphics.affichage_graphique import affiche
import sys

#######################################################################
#                Ajout d'un label a un mail                           #
#######################################################################
def ajoutLabel(service,labelId,messageId):
    """
    -Ajoute le label "labelId" au mail "messageId"
    -Pramètres :
        -``service`` : service de messagerie utilisé (ex : gmail)
        -``labelId`` : Identifiant deu label à ajouter.
        -``messageId`` : identifiantdu mail à labéliser.
    """
    userId = "me"
    body = {'addLabelIds': [labelId]}
   
    results_m = service.users().messages().list(userId='me').execute()
    results = service.users().messages().modify(userId=userId, id=messageId, body=body).execute()
    # la fonction modify renvoie le message que nous avons labélisé, pour les tests, il suffirai 
    # de retourner la variable `results` 

def gmailLabelisation(service,username,label =None,fenetre = None):
    """
    -	Démarre le machine learning sur la boite mail de l'utilisateur, 
        puis en fonction, labélise les mails non labélisés
    - Paramètres :
        -``service`` : service de messagerie utilisé (ex : gmail)
        -``username`` : identifiant de l'utilisateur de la boite mail (addresse mail).
        -``label`` : Zone de text de destination si en mode graphique, inexistant sinon.
        -``fenetre`` : Fenetre de destination pour affichage si en mode graphique, inexistante sinon.
    """
    affiche("--------------------------------------\n",0,label ,fenetre)
    affiche("MACHINE LEARNING\n",1,label,fenetre)
    mails_nonlab = csv_helper.toDict("NON_LABEL"+username)

    prediction = ml.supervised.supervisedWithNolabellingMail(username)
    affiche("--------------------------------------\n",0,label ,fenetre)

    if(prediction[0] == 0):
        affiche("Erreur lors de l'apprentissage automatique:\n1)Votre boite mail doit contenir un minimum de deux labels avec des mails triés\n2)Votre boite mail doit contenir des mails pas encore labélisés\n",0,label ,fenetre)
    else:
        affiche("Labélisation des mails en cours\n",1,label,fenetre)
        for i in range(len(prediction)):
            affiche(str(i)+"/"+str(len(prediction)-1)+"\n" ,1,label,fenetre)
            ajoutLabel(service = service,labelId = prediction[i],messageId = mails_nonlab[i]['id'])
