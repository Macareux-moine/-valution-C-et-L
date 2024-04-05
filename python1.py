import requests

def startrek():
    url = "https://stapi.co/api/v1/rest/astronomicalObject/search"
    
    try:
        response = requests.get(url)
        response.raise_for_status()  
        data = response.json()
        return data
    
    except requests.exceptions.RequestException as e:
        # Handle connection errors, timeouts, etc.
        print("Error:", e)
        return None
    
    except requests.exceptions.HTTPError as e:
        if response.status_code >= 400 and response.status_code < 500:
            raise Exception("Client Error: Check your request parameters or authorization.")
        elif response.status_code >= 500:
            raise Exception("Server Error: Please try again later.")
        else:
            raise Exception("HTTP Error:", e)
    
    except ValueError as e:
        print("Erreur JSON:", e)
        return None

try:
    S = startrek()
    if S:
        print(S)
    else:
        print("Pas de réponse")
except Exception as e:
    print("Erreur:", e)