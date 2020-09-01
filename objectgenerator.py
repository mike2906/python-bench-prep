"""Selects a random list of names from a file and assigns them random ages. Then selects
a random subset of these and produces a json file with them. Then loads the file again and
indicates which people are missing from the initial list.
""" 
import random
from random import randint
from random import sample
import json 
from collections import namedtuple



class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __eq__(self, other):
        return self.name == other.name and self.age == other.age

    def __repr__(self):
        return f"{self.name} is {self.age} years old."


def decode_person(ob):
    return Person(ob["name"], ob["age"])

def generate_people( age_max, no_of_people):
    """Reads a list of names from a file then selects a random number of them configured
    by no_of_people and assigns them ages up to age_max
    """
    try:
        people = []
        filename = "PotentialNames.txt"
        with open(filename) as myfile:
            for line in myfile:
                person = Person(line.rstrip('\n'),randint(1, age_max))
                people.append(person)
        people = random.sample(people, no_of_people)
        return people
    except FileNotFoundError:
        raise

def create_people_subset(people, subset_size):
    """Selects a subset of subset_size from the provided list, people"""
    return random.sample(people, subset_size)

def write_people_to_json_file(people_list):
    """Writes the provided list of people to a json file"""
    with open("people_subset.json", "w") as file:
        json.dump([ob.__dict__ for ob in people_list], file, indent=4)

def load_people_from_json_file():
    """Loads a list of people from a json file"""
    with open("people_subset.json") as file:
        return json.load(file, object_hook=decode_person)


def main(): 
    """Launcher."""
    try:
        age_max = 99
        no_of_people = 10
        subset_size = 2

        assert subset_size < no_of_people, "Error: subset_size too large. Must be smaller than no_of_people."

        people = generate_people(age_max,no_of_people)
        print('People: ', people)

        people_subset = create_people_subset(people,subset_size)
        print('Subset of people: ', people_subset)

        write_people_to_json_file(people_subset)
        
        people_from_json = load_people_from_json_file()
        print('People From File: ', people_from_json)

        print ("Missing people: ", [obj for obj in people if obj not in people_from_json])
    except (FileNotFoundError):
        print("File containing list of names has not been found.")
    except AssertionError as error:
        print(error)
        

if __name__ == "__main__": 
	main() 