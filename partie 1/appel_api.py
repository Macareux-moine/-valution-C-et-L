Import requests

def appel_api(query):
    if query.isdigit():  # Si l'entrée est un numéro, il s'agit d'un département
        url = f"https://geo.api.gouv.fr/departements/%7Bquery%7D/communes"
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

def comunes(commune):
    return commune.get("population", 0)

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
