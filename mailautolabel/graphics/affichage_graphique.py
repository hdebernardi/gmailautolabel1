def affiche(texte,suite,label=None,fenetre = None):
    """
    - Affiche un texte dans le label de la fenetre correspondante.
    - Paramètre :
        - ``texte`` : texte à afficher.
        - ``suite`` : si suite == 1 alors affiche le texte à la suite du texte déjà présent dans label, le remplace sinon
        - ``label`` : Zone de text de destination si en mode graphique, inexistant sinon.
            - ``fenetre`` : Fenetre de destination pour affichage si en mode graphique, inexistante sinon.
    """
    if(label == None):
        print(texte, end='')
    else:
        if(suite == 1):
            label['text'] += texte
            fenetre.update()
        else:
            label['text'] = texte
            fenetre.update()
