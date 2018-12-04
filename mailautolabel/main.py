import sys
import launcher_gmail
import launcher_imap
from graphics.interface_graphique import affichageTexteSimple

######################################################################
def main():
	"""
		Gère les arguments entrés par l'utilisateur.
		-graphics : Appelle l'interface graphique
		-imap : Appelle le launcher imap
		Sans arguments: Appel le launcher gmail
	"""
	
	
	flag_graphics = False
	flag_imap = False
	for arg in sys.argv:
		if arg == "-graphics":
			flag_graphics = True
		elif arg == "-imap":
			flag_imap = True
	
		
	
	if(flag_graphics==False):
 		print("----------------GMAIL AUTOLABEL 1----------------------")

 	# pour faciliter les tests
	hostname = 'imap.gmail.com'
	username = 'chucknorrism1luminy@gmail.com'
	password = 'm1luminy'
	
	############################## Argument -graphics
	if flag_graphics == True:
		affichageTexteSimple("L'affichage de texte fonctionne bien.\n"
					" Il suffit d'appeler la fonction avec texte.\n"
					" Texte etant ce qu'on veux afficher.",username=username)
		return

	############################## Argument -imap
	if flag_imap == True:
		launcher_imap.connectImap(hostname=hostname,username=username,password=password)
	else:
		launcher_gmail.connectGmail(username=username)
	

	
if __name__ == '__main__':
   main()
