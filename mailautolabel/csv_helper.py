import csv

#######################################################################
#return the absolute path of the file "username".csv
#Note: 
# cheminFich = 'data/{}.csv'.format(username) 
#It works but not portable on all OS

def cheminCsv(username):
    #gives the absolute path from where the script is started
    root=os.getcwd() 
    #donne data/username.csv ou data\username.csv si window ou linux
    rel_path = os.path.join("data", username+".csv")
    #chemin correcte du fichier
    abs_path = os.path.join(root, rel_path)
    return abs_path   


#######################################################################
#return 1 if path "username".csv is present, 0 if absent
def isPresent(username):
    cheminFich = cheminCsv(username = username)
    #we test if the file is present while trying to open it
    try:
        with open(cheminFich): pass
    except IOError:
        return 0 #file absent

    return 1 #file present


######################################################################
#returns a dictionary from a csv file
def csvToDict(username):
    list = [] #void list
    cheminFich = cheminCsv(username = username)

    with open(cheminFich, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        #we go through each line of the csv file
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
def save_mails(username, mails):
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
