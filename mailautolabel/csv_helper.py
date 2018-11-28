import csv
import os

#######################################################################
def getPath(username):
    """
    Renvoie le chemin absolu du fichier "username".csv
    - Note:
        cheminFich = 'data/{}.csv'.format(username) 
    Cela fonctionne mais probablement pas sur tout les OS
    """
    # Donne le chemin absolu d'où le script est démarré
    root = os.getcwd() 
    # Donne data/username.csv ou data\username.csv pour windows ou linux
    rel_path = os.path.join("data", username+".csv")
    # Chemin correct du fichier
    abs_path = os.path.join(root, rel_path)
    return abs_path   


#######################################################################
def isPresent(username):
    """
    Retourne 1 si le chemin "username".csv est présent, 0 sinon
    """
    filepath = getPath(username) 
    #Nous testons si le fichier est présent en essayant de l'ouvrir
    try:
        with open(filepath): pass
    except IOError:
        return 0 #Fichier absent

    return 1 #Fichier présent


######################################################################
def toDict(username):
    """
    Retourne un dictionnaire depuis un fichier csv
    """
    rv = []
    filepath = getPath(username)

    with open(filepath, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        # Nous parcourons chaque ligne du fichier csv
        for row in reader:            
            rv.append(row)
    
    return rv

################################################################################
import pandas as pd
def saveMails(username, mails):
	"""
    Créer un fichier csv depuis un dictionnaire
	"""
	filepath = getPath(username)
	df = pd.DataFrame(mails)
	df.to_csv(filepath)
