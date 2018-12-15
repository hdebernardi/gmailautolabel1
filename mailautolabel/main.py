import sys
import extraction.gmail.launcher_gmail as launcher_gmail
import graphics.interface_graphique as graphics

######################################################################
def main():
	"""
	-Gère les arguments entrés par l'utilisateur.
	-Paramètres :
		-``graphics`` : Appelle l'interface graphique
	"""
	
	print("----------------GMAIL AUTOLABEL 1----------------------")
	flag_graphics = False
	for arg in sys.argv:
		if arg == "-graphics":
			flag_graphics = True

		
	############################## Argument -graphics
	if flag_graphics == True:
		graphics.affichageTexteSimple("L'affichage de texte fonctionne bien.\n"
					" Il suffit d'appeler la fonction avec texte.\n"
					" Texte etant ce qu'on veux afficher.")
		return

	else:
		launcher_gmail.lancementGmail()
	

if __name__ == '__main__':
   main()
