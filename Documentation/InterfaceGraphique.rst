.. GmailAddon documentation master file, created by
   sphinx-quickstart on Mon Oct 29 09:36:13 2018.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

InterfaceGraphique
======================================


**Ce fichier gère l'affichage graphique et la récupération et gestions des labels et mails**


def triMail(lab,texte):
	- La fonction se sert recupere le label (zone de texte) et ecris "texte" dedans
	 
	 
def AffichageTexteSimple(texte):
	- Toute cette partie n'est pas dans une fonction spécifique pour pouvoir accéder au variable graphique dans tout le programme
	- Cette partie gère seulement l'affichage graphique
		- Pour la variable fenetre :
			1. La variable fenetre contient la fenêtre graphique
			2. fenetre.geometry("X*Y") permet de gérer la taille de la fenêtre
			3. fenetre.title("Titre") permet de définir le titre de la fenêtre
		- Pour la variable label : 
			1. Le mot clé Label définis des zones de texte de la bibliothèque tkinter
			2. label = Label(fenetre) Crée un Label de nom label et l'affecte a la fenêtre de nom fenetre
			3. label.configure(MotCle) Écris le texte dans label
				- MotCle -> text="Mon Texte" Ecris Mon Texte dans label
				- MotCle -> width = Taille Définis la taille de du label (entier)
				- MotCle -> font=police Affecte la police de nom police au texte de label
				- MotCle -> background='color' Applique la couleur color au background du label
				- MotCle -> anchor=CENTER Centre le texte au milieu du label
				- MotCle -> fg='color' Applique la couleur color au texte dans label
			4. label.pack() Affiche le label sur fenetre
		- tkinter.font.Font(family='Helvetica', size=20)
	   	 	1. family='Helvetica' Définie une police de texte
			2. size=Taille Définie une taille du texte, taille un entier
   	- PanedWindow(fenetre, orient=HORIZONTAL)
			1. PanedWindow crée une fenêtre graphique
			2. l'argument fenetre informe que la zone graphique est crée dans la fenêtre de nom fenetre
			3. orient Définie l'orientation de la zone graphique, horizontal ou vertical
	- pack(side=TOP,expand=Y, fill=BOTH, pady=2, padx=2)
			1. expand Ce mot clé permet a l'objet de prendre toute la place disponible sur l'axe désigne (X ou Y)
			2. pady et padx donnent les marges de l'objet
	- p.add(AutreObjetDeTkinter) Ajoute l'objet AutreObjetDeTkinter a la fenêtre ou a l'objet graphique p
	- Button(fenetre, text="Trier les mails",width=20, command=start2)
			1. Le mot clé Button crée un bouton
			2. text="Texte" Écris Texte dans le bouton
			3. witdh=TAILLE Donne la taille TAILLE au bouton (entier)
			4. command=NomFonction Execute la fonction NomFonction lorsque on clique sur le bouton 
		 
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
