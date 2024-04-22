import requests

def Sélection():
    choice = choice_var.get()
    if choice == "Ville":
        Ville()
    elif choice == "Département":
        departement()
    elif choice == "Code postal":
        code_postal()

def appel_api(query):
    if query.isdigit():  # Si l'entrée est un numéro, il s'agit d'un département
        url = f"https://geo.api.gouv.fr/departements/{query}/communes"
    else:  # Sinon, c'est le nom d'une ville
        url = f"https://geo.api.gouv.fr/communes?nom={query}&fields=population"

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return data if isinstance(data, list) else [data]
    except requests.exceptions.HTTPError as err:
        print(f"Erreur lors de la requête à l'API : {err}")
        return None
    except requests.exceptions.RequestException as err:
        print(f"Erreur lors de la requête à l'API : {err}")
        return None
    
def comunes(communes_list):
    total_population = 0
    if isinstance(communes_list, list):
        for commune in communes_list:
            total_population += commune.get("population", 0)
    else:
        total_population = communes_list.get("population", 0)
    return total_population

def departement():
    url = "https://geo.api.gouv.fr/departements"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return data
    except requests.exceptions.HTTPError as err:
        print(f"Erreur lors de la requête à l'API : {err}")
        return None
    except requests.exceptions.RequestException as err:
        print(f"Erreur lors de la requête à l'API : {err}")
        return None

def code_postal(query):
    url = f"https://geo.api.gouv.fr/communes?codePostal={query}&fields=population"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        population = sum(comunes(commune) for commune in data)
        return population
    except requests.exceptions.HTTPError as err:
        print(f"Erreur lors de la requête à l'API : {err}")
        return None
    except requests.exceptions.RequestException as err:
        print(f"Erreur lors de la requête à l'API : {err}")
        return None

