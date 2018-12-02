from tkinter import * 
import tkinter.font
from tkinter.messagebox import *
import sys

#Fonction triMail qui devrait trier les mails et actualiser l'affichage
def triMail(lab,texte):
	lab['text'] = texte	#Ajout de texte au label


def affichageTexteSimple(username):
	#Création d'une fenetre 
	fenetre = Tk()	
	fenetre.geometry("1000x1000") #Définition de la taille de base de la fenètre
	fenetre.title("Interface projet auto-labbel gmail")	#Nom de la fenètre

	#Création du label pour afficher du texte
	police=tkinter.font.Font(family='Helvetica', size=20)	#Définition de la police pour le texte dans le label

	label = Label(fenetre)			#Création zone pour texte
	label.configure(text="Bienvenue dans le logiciel d'automatisation de labels !")	#Texte à écrire
	label.configure(width=106)		#Taille de la zone de texte
	label.configure(font=police)	#On applique la police au label
	label.pack()					#On place la zone
	
	
	#Nouvelle police de texte pour l'affichage des opérations sur les mails
	police2=tkinter.font.Font(family='Helvetica', size=20)


	#Création de la zone pour le bouton et pour l'affichage des mail
	p = PanedWindow(fenetre, orient=HORIZONTAL)
	lab=Label(p, background='black',text="Rien pour le moment",fg='green', anchor=CENTER,width=1000)
	lab.configure(font=police2)
	#fg pour régler la couleur du texte
	#width règle la taille du label
	#background gère la couleur du fond
	p.pack(side=TOP,expand=Y, fill=BOTH, pady=2, padx=2)
	#pady et padx gère les "marges"
	#text="AAA"
	#p.add(Button(fenetre, text="Trier les mails",width=20, command=lambda:mail_extractor.main(sys.argv)))
	#p.add(Button(fenetre, text="Trier les mails",width=20, command=lambda:mail_labelizer.main(sys.argv))) 
	#Si pas lambda alors la fonction se lance en auto
	#Bouton de tri des mails et l'affichage
	#Il a une valeur texte de base
	#Lorsque l'on clique dessus on appelle la fonction triMail
	p.add(lab) #2ème rectangle, affichage des operations effectuées
	p.pack()
	fenetre.mainloop()
	
	

	
