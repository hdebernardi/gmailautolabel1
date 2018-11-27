import csv
import os

#######################################################################
#return the absolute path of the file "username".csv
#Note: 
# cheminFich = 'data/{}.csv'.format(username) 
#It works but not portable on all OS

def get_path(username):
    """
    return the absolute path of the file "username".csv
    Note: 
    filepath = 'data/{}.csv'.format(username) 
    It works but not portable on all OS
    """
    # gives the absolute path from where the script is started
    root = os.getcwd() 
    # gives data/username.csv or data\username.csv for windows or linux
    rel_path = os.path.join("data", username+".csv")
    # correct path of the file
    abs_path = os.path.join(root, rel_path)
    return abs_path   


#######################################################################
def is_present(username):
    """
    return 1 if path "username".csv is present, 0 if absent
    """
    filepath = get_path(username) 
    #we test if the file is present while trying to open it
    try:
        with open(filepath): pass
    except IOError:
        return 0 #file absent

    return 1 #file present


######################################################################
def to_dict(username):
    """
    returns a dictionary from a csv file
    """
    rv = []
    filepath = get_path(username)

    with open(filepath, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        # we go through each line of the csv file
        for row in reader:            
            rv.append(row)
    
    return rv

################################################################################
import pandas as pd
def save_mails(username, mails):
	filepath = get_path(username)
	df = pd.DataFrame(mails)
	df.to_csv(filepath)
