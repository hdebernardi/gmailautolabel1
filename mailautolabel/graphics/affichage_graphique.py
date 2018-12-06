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
