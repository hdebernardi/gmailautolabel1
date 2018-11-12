from tkinter import * 
import tkinter.font
from tkinter.messagebox import *
import time



#fonction triMail qui devrais trier les mails et actualiser l'affichage
def triMail(lab,texte):
	lab['text'] = texte	#Ajout de texte au label


def AffichageTexteSimple(texte):
	#Creation d'une fenetre 
	fenetre = Tk()	
	fenetre.geometry("1000x1000") #Definission de la taille de base de la fenetre
	fenetre.title("Interface projet auto-labbel gmail")	#Nom de la fenetre

	#Creation du label pour afficher du texte
	police=tkinter.font.Font(family='Helvetica', size=20)	#Definition de la police pour le texte dans le label

	label = Label(fenetre)			#Creation zone pour texte
	label.configure(text="Bienveue dans le logiciel d'automatisation de labels !")	#Texte a ecrire
	label.configure(width=106)		#Taille de la zone de texte
	label.configure(font=police);		#On applique la police au label
	label.pack()				#On place la zone
	
	
	#Nouvelle police de texte pour l'affichage des operations sur les mails
	police2=tkinter.font.Font(family='Helvetica', size=20)


	#Creation de la zone pour le bouton et pour l'affichage des mail
	p = PanedWindow(fenetre, orient=HORIZONTAL)
	lab=Label(p, background='black',text="Rien pour le moment",fg='green', anchor=CENTER,width=1000)
	lab.configure(font=police2);
	#fg pour regler la couleur du texte
	#width regle la taille du label
	#background gere la couleur du fond
	p.pack(side=TOP,expand=Y, fill=BOTH, pady=2, padx=2)
	#pady et padx gere les "marges"
	text="AAA"
	p.add(Button(fenetre, text="Trier les mails",width=20, command=lambda:triMail(lab,texte))) 
	#Si pas lambda alors la fonction se lance en auto
	#Boutton de tri des mails et l'affichage
	#Il a une valeur texte de base
	#Lorsque on clique dessus on appelle la fonction triMail
	p.add(lab) #2eme rectangle, affichage des operation effectuee
	p.pack()
	fenetre.mainloop()
	
	

	
