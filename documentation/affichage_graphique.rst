.. GmailAddon documentation master file, created by
   sphinx-quickstart on Mon Oct 29 09:36:13 2018.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

affichage_graphique
======================================
def affiche(texte,suite,label=None,fenetre = None):
    -``texte`` : texte à afficher.

	-``suite`` : si suite == 1 alors affiche le texte à la suite du texte déjà présent dans label, le remplace sinon

	-``label`` : Zone de text de destination si en mode graphique, inexistant sinon.
    
    -``fenetre`` : Fenetre de destination pour affichage si en mode graphique, inexistante sinon.
