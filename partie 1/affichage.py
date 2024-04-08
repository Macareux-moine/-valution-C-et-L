from affichage import ville, departement, code_postal
import tkinter as tk

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
submit_button = tk.Button(root, text="Valider", command=on_choice_selected)
submit_button.pack()

root.mainloop()
