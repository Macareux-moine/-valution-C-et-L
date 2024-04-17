import tkinter as tk
import affichage
import appel_api

def afficher_population():
    query = affichage.get_input()  # Obtenir la requête de l'utilisateur depuis l'interface
    data = appel_api.appel_api(query)  # Appeler l'API avec la requête
    if data:
        if isinstance(data, list):
            # Si la réponse est une liste de communes, afficher la somme de la population
            total_population = appel_api.somme_habitants(data)
            affichage.show_message(f"Population totale : {total_population}")
        else:
            # Sinon, afficher la population de la commune demandée
            population = appel_api.comunes(data)
            affichage.show_message(f"Population : {population}")
    else:
        affichage.show_message("Erreur : Impossible de récupérer les données.")

def main():
    affichage.create_main_window(afficher_population)

if __name__ == "__main__":
    main()
