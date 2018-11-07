import os

#retourne 1 si le fichier "username.csv" est présent, 0 si absent
def isPresent(username):
    #donne le chemin absolu d'où est lancé le script
    root=os.getcwd() 
    #donne data/username.csv ou data\username.csv si window ou linux
    rel_path = os.path.join("data",username+".csv")
    #chemin correcte du fichier
    abs_path = os.path.join(root, rel_path)

    #on test si le fichier est présent en tentant de l'ouvrir
    try:
        with open(abs_path): pass
    except IOError:
        return 0 #fichier absent

    return 1 #fichier présent

