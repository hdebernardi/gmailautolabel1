import sys
import launcher_gmail
import launcher_imap
from graphics.InterfaceGraphique import AffichageTexteSimple

######################################################################
def main():
	"""
		Gère les arguments entrés par l'utilisateur.
		-graphics Appel l'interface graphique
		-imap Appel le launcher imap
		Sans arguments: Appel le launcher gmail
	"""
	
	print("----------------GMAIL AUTOLABEL 1----------------------")

	flag_graphics = False
	flag_imap = False
	for arg in sys.argv:
		if arg == "-graphics":
			flag_graphics = True
		elif arg == "-imap":
			flag_imap = True	
 
	############################## Argument -graphics
	if flag_graphics == True:
		AffichageTexteSimple("L'affichage de texte fonctionne bien.\n"
					" Il suffit d'appeler la fonction avec texte.\n"
					" Texte etant ce qu'on veux afficher.")

	############################## Argument -imap
	# pour faciliter les tests
	hostname = 'imap.gmail.com'
	username = 'chucknorrism1luminy@gmail.com'
	password = 'm1-luminy'

	if flag_imap == True:
		launcherImap.connectImap(hostname=hostname,username=username,password=password)
	else:
		launcherGmail.connectGmail(username = username)
	

	
if __name__ == '__main__':
   main()
