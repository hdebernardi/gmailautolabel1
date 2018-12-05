import sys
import extraction.gmail.launcher_gmail as launcher_gmail
import extraction.imap.launcher_imap as launcher_imap
import graphics.interface_graphique as graphics

######################################################################
def main():
	"""
		Gère les arguments entrés par l'utilisateur.
		-graphics : Appelle l'interface graphique
		-imap : Appelle le launcher imap
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
		graphics.affichageTexteSimple("L'affichage de texte fonctionne bien.\n"
					" Il suffit d'appeler la fonction avec texte.\n"
					" Texte etant ce qu'on veux afficher.")
		return

	############################## Argument -imap
	if flag_imap == True:
		username = input("Entrer l'adresse imap: ")
		hostname = input("Entrer votre adresse email: ")
		password = input("Entrer votre mot de passe: ")
		launcher_imap.lancementImap(hostname=hostname,username=username,password=password)
	else:
		launcher_gmail.lancementGmail()
	

	
if __name__ == '__main__':
   main()
