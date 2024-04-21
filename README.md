# Partie 1 

api geo.api.gouv.fr 
en fontion du département ou de la ville afficher le nombre habitant 
et faire la somme des habitant 


Il nous foudrais module/ class qui gere appel api. 
 - avec la possiblité d'entré url de api, puis le parametre de l'api pour qu'il nous retroune les valeur demande 
 avec une gestion du type de donné json, csv, dictionaire ect...
  eventuellment avec un fenetre appel pour que utilisateur si retrouve facilement
  
  un fonction calcul pour la somme des habitant dans un departement
  
  dans appel_api.py
def appel_api # pour  faire appel request

def comunes # pour recuperer la valeur "population" de api 
return commune.get("population",0)# un truc dans le genre 

def departement # pour recupere la liste des departemens 

 dans le fichier main.py # parti principal du fichier qui fera appel au autre .py
 
 
def  selection () # pour choisir les posibilité entre ville et département voir avec le code postal
def ville # qui va afficher une fenetre de sélection ville
def resulat() # qui va demande le nom de la ville ( dans une fentre tkdinter
def departement()# qui va qui va afficher une fenetre de sélection le départemen
def resultat # avec ici le calcule d'une somme de toute les ville du departement avec une focntion de type 
population = sum(....)
def code_postal # affiche la posibilité de taper un code postal 
def resultat# # cherche et affiche le resulat trouve par appel_api 


une partie sur l'affichage des donnée ou le faire dans un autre .py a reflechir 



partie 2 

def lire_fichier(chemein_fichier)
whit open(chemein_fichier,'r') # un truc dans le genre, je me rappel plus excatement de la sintax

def sélection() # sois ssh sois ftp avec une demande de choix 
choice= choice_var.get()
if choise == 'ssh':
bruteforce_ssh()
else 
if choise == 'ftp':
bruteforce_ftp()

def bruteforce_ssh() 

# va cherche le module bruteforce_ssh.py et associe la liste 
utilisateur rentre le chemin de la liste,

def bruteforce_ftp
# va cherche le module bruteforce_ftp.py et associe la liste 
utilisateur rentre le chemin de la liste,

 
 
 partie sur affichage d'un barre de pourcentage avec le temps écoulé voir estimé, 
 
 
 
 
 
 
Qui travail sur quoi ?
projet 1: 
pour la fichier appel_api.py
pour la fichier affichage.py
pour la fichier main()

Projet 2: 
Pour la fichier bruteforce_ssh.py
Pour le fichier bruteforce_ftp.py
pour le fichier main.py
pour le fichier affichageprograssion.py 
