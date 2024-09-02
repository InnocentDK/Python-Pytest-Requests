import requests
import json

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'c6839c9b56d60bc52fbae19b461b0943'
HEADER = {'Content-Type':'application/json', 'trainer_token':TOKEN}
TRAINER_ID = 4595

response = requests.post(url = f'{URL}/pokemons', headers=HEADER, json={
    "name": "Jackson",
    "photo_id": 10
})

print(response.text)

response = requests.put(url = f'{URL}/pokemons', headers=HEADER, json={
    "pokemon_id": "65781",
    "name": "Mick",
    "photo_id": 10
})

print(response.text)

response = requests.post(url = f'{URL}/trainers/add_pokeball', headers=HEADER, json={
    "pokemon_id": "65781"
})

print(response.text)