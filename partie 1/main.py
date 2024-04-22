import requests
import tkinter as tk
from tkinter import messagebox, ttk
from appel_api import appel_api, comunes, departement


def Sélection():
    choice = choice_var.get()
    if choice == "Ville":
        Ville()
    elif choice == "Département":
        departement()
    elif choice == "Code postal":
        code_postal()

def Ville():
    window = tk.Toplevel(root)
    window.title("Recherche par Ville")

    def resultat():
        query = entry_ville.get()
        if not query:
            messagebox.showerror("Erreur", "Veuillez entrer le nom de la ville.")
            return

        result = appel_api(query)
        if result is not None:
            if isinstance(result, list):
                population = sum(comunes(commune) for commune in result)
            else:
                population = comunes(result)
            messagebox.showinfo("Résultat", f"La population de {query} est de : {population}")

    label = tk.Label(window, text="Entrez le nom de la ville :")
    label.pack()
    entry_ville = tk.Entry(window)
    entry_ville.pack()
    submit_button = tk.Button(window, text="Valider", command=resultat)
    submit_button.pack()

def departement():
    window = tk.Toplevel(root)
    window.title("Recherche par Département")

    def resultat():
        query = entry_departement.get()
        if not query:
            messagebox.showerror("Erreur", "Veuillez entrer le numéro du département.")
            return

        result = appel_api(query)
        if result is not None:
            population = sum(comunes(commune) for commune in result)
            messagebox.showinfo("Résultat", f"La somme des habitants du département {query} est de : {population}")

    label = tk.Label(window, text="Entrez le numéro du département :")
    label.pack()
    entry_departement = tk.Entry(window)
    entry_departement.pack()
    submit_button = tk.Button(window, text="Valider", command=resultat)
    submit_button.pack()
    

# Création de la fenêtre principale
root = tk.Tk()
root.title("API Gouv.fr")

# Choix entre Ville, Département ou Code postal
label_choice = tk.Label(root, text="Choisissez votre recherche :")
label_choice.pack()
choices = ["Ville", "Département", "Code postal"]
choice_var = tk.StringVar(root)
choice_var.set(choices[0])  # Valeur par défaut : Ville
choice_menu = tk.OptionMenu(root, choice_var, *choices)
choice_menu.pack()

# Bouton pour valider le choix
submit_button = tk.Button(root, text="Valider", command=Sélection)
submit_button.pack()

root.mainloop()
