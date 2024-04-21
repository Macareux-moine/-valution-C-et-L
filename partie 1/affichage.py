import tkinter as tk
from Projet.P1.appel_api import appel_api, comunes

def on_choice_selected():
    selected_choice = choice_var.get()
    query = input_entry.get()

    if selected_choice == "Ville":
        population = comunes(appel_api(query))
    elif selected_choice == "Département":
        population = sum([comunes(commune) for commune in appel_api(query)])
    elif selected_choice == "Code postal":
        population = sum([comunes(commune) for commune in appel_api(query)])

    if population:
        result_label.config(text=f"Population : {population}")
    else:
        result_label.config(text="Aucune donnée disponible")

root = tk.Tk()
root.title("API Gouv.fr")

label_choice = tk.Label(root, text="Choisissez votre recherche 
label_choice.pack()

choices = ["Ville", "Département", "Code postal"]
choice_var = tk.StringVar(root)
choice_var.set(choices[0])
choice_menu = tk.OptionMenu(root, choice_var, *choices)
choice_menu.pack()

input_label = tk.Label(root, text="Entrez votre recherche 
input_label.pack()
input_entry = tk.Entry(root)
input_entry.pack()

submit_button = tk.Button(root, text="Valider", command=on_choice_selected)
submit_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()
