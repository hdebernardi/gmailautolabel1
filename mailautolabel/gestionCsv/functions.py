import os
import csv

#######################################################################
#renvoi le chemin absolu du fichier "username".csv
#Remaque: 
# cheminFich = 'data/{}.csv'.format(username) 
#Cela fonctionne mais pas portable sur tous les os

def cheminCsv(username):
    #donne le chemin absolu d'où est lancé le script
    root=os.getcwd() 
    #donne data/username.csv ou data\username.csv si window ou linux
    rel_path = os.path.join("data",username+".csv")
    #chemin correcte du fichier
    abs_path = os.path.join(root, rel_path)
    return abs_path   


#######################################################################
#retourne 1 si le fichier "username".csv est présent, 0 si absent
def isPresent(username):
    cheminFich = cheminCsv(username = username)
    #on test si le fichier est présent en tentant de l'ouvrir
    try:
        with open(cheminFich): pass
    except IOError:
        return 0 #fichier absent

    return 1 #fichier présent


######################################################################
#retourne une liste à partir d'un fichier csv
def csvToList(username):
    list = [] #on crée une liste vide
    cheminFich = cheminCsv(username = username)

    with open(cheminFich, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        #on parcourt chaque lignes du fichier csv
        for row in reader:            
            list.append(row)
    
    return list
    
    '''
    Pour afficher la list
    for var in list:
        print('------------------------------')
        print("Message-ID",var['Message-ID'])
        print("Date",var['Date'])
        print("From",var['From'])
        print("To",var['To'])
        print("Subject",var['Subject'])
        print("Body",var['Body'])
        print("Content-type",var['Content-type'])
    '''

################################################################################
def save_mails_csv(username, mails):
	filename = cheminCsv(username)
	try:
		file = open(filename, 'r')
	except IOError:
		file = open(filename, 'w')
	
	keys = mails[0].keys()
	with open(filename, 'w') as csvfile:
		writer = csv.DictWriter(csvfile, keys)
		writer.writeheader()
		writer.writerows(mails)
