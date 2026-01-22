import os
import requests
from dotenv import load_dotenv

# Lädt die Variablen aus der .env Datei in das System
load_dotenv()

# Greift auf die Variable zu
API_KEY = os.getenv('API_KEY')
API_URL = 'https://api.api-ninjas.com/v1/animals?name={}'


def fetch_data(animal_name):
    # Falls der Key nicht gefunden wurde, geben wir eine Warnung aus
    if not API_KEY:
        print("Fehler: API_KEY wurde nicht in der .env Datei gefunden!")
        return []

    response = requests.get(
        API_URL.format(animal_name),
        headers={'X-Api-Key': API_KEY}
    )

    if response.status_code == 200:
        return response.json()
    return []