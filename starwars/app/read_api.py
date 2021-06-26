import requests
from pprint import pprint


def read_api():
    response_one = requests.get("https://swapi.dev/api/starships")
    response_two= requests.get("https://swapi.dev/api/starships/?page=2")
    response_three = requests.get("https://swapi.dev/api/starships/?page=3")
    response_four = requests.get("https://swapi.dev/api/starships/?page=4")
    return response_one.json(), response_two.json(), response_three.json(), response_four.json()

pprint(type(read_api()))