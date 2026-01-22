import os
import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv('API_KEY')
API_URL = 'https://api.api-ninjas.com/v1/animals?name={}'

def fetch_data(animal_name):
    """Holt Daten von der API."""
    response = requests.get(API_URL.format(animal_name), headers={'X-Api-Key': API_KEY})
    return response.json() if response.status_code == 200 else []