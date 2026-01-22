import requests

API_KEY = 'tJcOUz1ik7BJqpzaYiw8LwffYWtNdOoYLzwuHav7'

def fetch_data(animal_name): # <--- Prüfe diesen Namen!
    api_url = f'https://api.api-ninjas.com/v1/animals?name={animal_name}'
    response = requests.get(api_url, headers={'X-Api-Key': API_KEY})
    if response.status_code == 200:
        return response.json()
    return []