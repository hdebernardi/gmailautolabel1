from tkinter import * 
import tkinter.font
from tkinter.messagebox import *
import time
import extraction.gmail.launcher_gmail

def affichageTexteSimple(texte):
	'''
	-Toute cette partie n'est pas dans une fonction spécifique pour pouvoir accéder au variable graphique dans tout le programme
	-Cette partie gère seulement l'affichage graphique
		-Pour la variable fenetre :
			a-La variable fenetre contient la fenêtre graphique
			b-fenetre.geometry("X*Y") permet de gérer la taille de la fenêtre
			c-fenetre.title("Titre") permet de définir le titre de la fenêtre
			
		-Pour la variable label :
			a-Le mot clé Label définis des zones de texte de la bibliothèque tkinter
			b-label = Label(fenetre) Crée un Label de nom label et l'affecte a la fenêtre de nom fenetre
			c-label.configure(MotCle) Écris le texte dans label
				-MotCle -> text="Mon Texte" Ecris Mon Texte dans label
				-MotCle -> width = Taille Définis la taille de du label (entier)
				-MotCle -> font=police Affecte la police de nom police au texte de label
				-MotCle -> background='color' Applique la couleur color au background du label
				-MotCle -> anchor=CENTER Centre le texte au milieu du label
				-MotCle -> fg='color' Applique la couleur color au texte dans label
			d-label.pack() Affiche le label sur fenetre
			
		-tkinter.font.Font(family='Helvetica', size=20)
			a-family='Helvetica' Définie une police de texte
			b-size=Taille Définie une taille du texte, taille un entier
			
		-PanedWindow(fenetre, orient=HORIZONTAL)
			i-PanedWindow crée une fenêtre graphique
			ii-l'argument fenetre informe que la zone graphique est crée dans la fenêtre de nom fenetre
			iii-orient Définie l'orientation de la zone graphique, horizontal ou vertical
			
		-pack(side=TOP,expand=Y, fill=BOTH, pady=2, padx=2)
			i-expand Ce mot clé permet a l'objet de prendre toute la place disponible sur l'axe désigne (X ou Y)
			ii-pady et padx donnent les marges de l'objet
		-p.add(AutreObjetDeTkinter) Ajoute l'objet AutreObjetDeTkinter a la fenêtre ou a l'objet graphique p
		
		-Button(fenetre, text="Trier les mails",width=20, command=start2)
			i-Le mot clé Button crée un bouton
			ii-text="Texte" Écris Texte dans le bouton
			iii-witdh=TAILLE Donne la taille TAILLE au bouton (entier)
			iv-command=NomFonction Execute la fonction NomFonction lorsque on clique sur le bouton
	'''

	#Création d'une fenetre 
	fenetre = Tk()	
	fenetre.geometry("1000x1000") #Définition de la taille de base de la fenètre
	fenetre.title("Interface projet auto-labbel gmail")	#Nom de la fenètre
	#fenetre.configure(highlightbackground='black',highlightcolor='black')
	fenetre.config(bg='black')

	#Création du label pour afficher du texte
	police=tkinter.font.Font(family='Helvetica', size=20)	#Définition de la police pour le texte dans le label

	label = Label(fenetre)			#Création zone pour texte
	label.configure(text="Bienvenue dans le logiciel d'automatisation de labels !",fg='gray60')	#Texte à écrire
	label.configure(width=106)		#Taille de la zone de texte
	label.configure(font=police)	#On applique la police au label
	label.configure(bg='gray35',highlightbackground='black',highlightcolor='black')
	label.pack()					#On place la zone
	
	
	#Nouvelle police de texte pour l'affichage des opérations sur les mails
	police2=tkinter.font.Font(family='Helvetica', size=20)


	#Création de la zone pour le bouton et pour l'affichage des mail
	p = PanedWindow(fenetre, orient=HORIZONTAL,bg='black')
	lab=Label(p,highlightbackground='black',highlightcolor='black', background='gray18',text="Rien pour le moment",fg='gray60', anchor=CENTER,width=1000)
	lab.configure(font=police2);
	#fg pour régler la couleur du texte
	#width règle la taille du label
	#background gère la couleur du fond
	p.pack(side=TOP,expand=Y, fill=BOTH)
	#pady et padx gère les "marges"
	p.add(Button(fenetre,highlightbackground='black',highlightcolor='black',bg='gray35', text="Trier les mails",fg='gray60',width=20, command=lambda:extraction.gmail.launcher_gmail.lancementGmail(label=lab,fenetre=fenetre))) 
	#Si pas lambda alors la fonction se lance en auto
	#Bouton de tri des mails et l'affichage
	#Il a une valeur texte de base
	#Lorsque l'on clique dessus on appelle la fonction triMail
	p.add(lab) #2ème rectangle, affichage des operations effectuées
	p.pack()
	fenetre.mainloop()
	
	

	
