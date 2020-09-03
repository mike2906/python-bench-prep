import json 

def write_people_to_json_file(people):
    """Writes the provided list of people to a json file"""
    with open("people_subset.json", "w") as file:
        #json.dump([ob.__dict__ for ob in people_list], file, indent=4)
        json.dump(people, file, default=lambda o: o.__dict__, sort_keys=True, indent=4)