# mailautolabel
Toutes les informations sont détaillées dans le wiki. Vous trouverez ci dessous un résumé très restreint de l'utilisation du logiciel.

## A quoi sert le logiciel ?

Le logiciel mailautolabel est un classifieur automatique de mails. Il se connecte à une messagerie Gmail, récupère les mails et les dossiers et les envoient dans un algorithme de machine learning. A la fin de cet algorithme, tous les mails qui ne possèdent pas un label sont classés automatiquement avec le label leurs correspondant le plus.

## Comment l'installer ?

### Prérequis

Pour utiliser ce projet, vous devez déjà avoir installé:

python3
     https://www.python.org/
     
virtualenv
    https://virtualenv.pypa.io/en/latest/

make
     https://www.gnu.org/software/make/

### Installation des librairies

Ensuite, naviguez simplement à la racine de ce projet et exécutez:

 -virtualenv -p python3 env
 
 -source env/bin/activate
 
 -make

## Comment le lancer ?

 -cd mailautolabel
 
 -python3 main.py

## Le projet évolue !
https://github.com/hdebernardi/MailAutoLabel
