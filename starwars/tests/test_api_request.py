from starwars.app.api_request import api_request


def test_api_request():
    assert api_request("https://swapi.dev/api/starships").status_code == 200
