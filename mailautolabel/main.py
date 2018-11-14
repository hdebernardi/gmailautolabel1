import sys
import launcherGmail
import launcherImap
from graphics.InterfaceGraphique import AffichageTexteSimple

###################################################################
#return hostname,username,password by default or cho
def argMail(flag_default):
	# read configuration variables from config.ini file
	if flag_default == True:
		hostname = 'imap.gmail.com'
		username = 'm1.autolabel1@gmail.com'
		password = 'm1-luminy'
	#user enter variables
	elif flag_default == False:
		hostname = input("Enter imap adress : ")
		username = input("Enter mail : ")
		password = input("Enter password : ")
	
	return (hostname,username,password)

######################################################################
def main():
	print("----------------GMAIL AUTOLABEL 1----------------------")

	flag_graphics = False
	flag_default = False
	flag_imap = False
	for arg in sys.argv:
		if arg == "-graphics":
			flag_graphics = True
		elif arg == "-default":
			flag_default = True
		elif arg == "-imap":
			flag_imap = True	
 
	############################## Argument -graphics
	if flag_graphics == True:
		AffichageTexteSimple("L'affichage de texte fonctionne bien.\n"
					" Il suffit d'appeler la fonction avec texte.\n"
					" Texte etant ce qu'on veux afficher.")

	############################## Argument -mail
	connect = argMail(flag_default = flag_default)
	#On récupère hostname, username,password
	hostname = connect[0]
	username = connect[1]
	password = connect[2]

	
	index= username.find('@gmail.com')
	#Si l'utilisateur veut utiliser une connection imap
	if flag_imap == True:
		launcherImap.connectImap( hostname=hostname, username=username, password=password)
	#Si il ne précise pas et que l'adresse mail saisi n'est pas gmail on utilise une connexion imap
	elif index == -1:
		launcherImap.connectImap( hostname=hostname, username=username, password=password)
	#Sinon l'utilisateur possède une adresse gmail 
	else:
		launcherGmail.connectGmail(username = username)
	

	
if __name__ == '__main__':
   main()
