from starwars.app.changing_pilot_url import *

#Test that checks that the url for the pilots has been changed into their respective Object Ids
def test_change_pilot_url():
    assert type(starships["pilots"]) == type(characters["_id"])