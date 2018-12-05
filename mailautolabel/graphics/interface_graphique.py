from tkinter import * 
import tkinter.font
from tkinter.messagebox import *
import time
import extraction.gmail.launcher_gmail

def affiche(texte,suite,label=None,fenetre = None):
	if(label == None):
		print(texte, end='')
	else:
		if(suite == 1):
			label['text'] += texte
			fenetre.update()
		else:
			label['text'] = texte
			fenetre.update()

def affichageTexteSimple(texte):
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
	
	

	
