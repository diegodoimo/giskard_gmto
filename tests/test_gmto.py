import json 
from gmto.backend import get_proba
from gmto.web.helpers import read_empire_data, read_falcon_data


def test_get_proba():
    
    folders = ['example1', 'example2', 'example3', 'example4']

    for folder in folders:

        empire_data = read_empire_data(f"tests/examples/{folder}/empire.json")
        falcon_data = read_falcon_data(f"tests/examples/{folder}/millennium-falcon.json")

        with open(f"tests/examples/{folder}/answer.json", 'r') as f:
            answer = json.load(f)

        assert (answer['odds'] == get_proba(empire_data = empire_data, falcon_data = falcon_data))


