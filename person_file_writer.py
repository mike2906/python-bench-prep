import json 
import functools
from people import PeopleEncoder, People

def write_people_to_json_file(people):
    """Writes the provided list of people to a json file"""
    with open("people_subset.json", "w") as file:
        #print("people dict: ", people.__dict__)
        #json.dump(people, file, default=lambda o: o.__dict__, sort_keys=True, indent=4)
        json.dump(people.to_json(), file, cls=PeopleEncoder)
    return 'wrote to file'

