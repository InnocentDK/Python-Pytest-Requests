import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'c6839c9b56d60bc52fbae19b461b0943'
HEADER = {'Content-Type':'application/json', 'trainer_token':TOKEN}
TRAINER_ID = 4595

def test_status_code():
    response = requests.get(url = f'{URL}/trainers')
    assert response.status_code == 200

def test_trainer_name():
    response = requests.get(url = f'{URL}/trainers', params={'trainer_id' : TRAINER_ID})
    assert response.json()["data"][0]["trainer_name"] == 'Денис'