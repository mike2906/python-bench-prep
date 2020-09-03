"""Selects a random list of names from a file and assigns them random ages. Then selects
a random subset of these and produces a json file with them. Then loads the file again and
indicates which people are missing from the initial list.
""" 
import random
from random import randint
from random import sample
import json 
from collections import namedtuple
from typing import List
import person_file_writer
from people import People, Person




class People(object):
    def __init__(self, people: List[Person]):
        self.people = people

    @classmethod
    def from_json(cls, data):
        people = list(map(Person.from_json, data["people"]))
        return cls(people)
    
    def __eq__(self, other):
        return self.people == other.people

#def decode_person(ob):
#    return Person(ob["name"], ob["age"])

def generate_people( age_max, no_of_people, filename):
    """Reads a list of names from a file then selects a random number of them configured
    by no_of_people and assigns them ages up to age_max
    """
    try:
        people = []
        with open(filename) as myfile:
            for line in myfile:
                person = Person(line.rstrip('\n'),randint(1, age_max))
                people.append(person)
        people = random.sample(people, no_of_people)
        return People(people)
    except (FileNotFoundError, ValueError):
        raise

def create_people_subset(people, subset_size):
    """Selects a subset of subset_size from the provided list, people"""
    return People(random.sample(people.people, subset_size))




def load_people_from_json_file():
    """Loads a list of people from a json file"""
    with open("people_subset.json") as file:
        #return json.load(file, object_hook=decode_person)
        return People.from_json(json.load(file))

def main(): 
    try:
        #Max age to assign
        age_max = 99
        #How many people to generate (<=200)
        no_of_people = 10
        #How many people should be in subset
        subset_size = 2
        #Filename of file which contains potential names to use to generate people
        potential_names_filename = "PotentialNames.txt"

        assert subset_size < no_of_people, "Error: subset_size too large. Must be smaller than no_of_people."

        people = generate_people(age_max,no_of_people, potential_names_filename)
        print('People full list: ', people.people)

        people_subset = create_people_subset(people,subset_size)
        print('Subset of people: ', people_subset.people)

        person_file_writer.write_people_to_json_file(people_subset)

        people_from_json = load_people_from_json_file()
        print('People From File: ', people_from_json.people)

        missing_people = [obj for obj in people.people if obj not in people_from_json.people]
        print ("Missing people: ", missing_people)
        
    except (FileNotFoundError):
        print("File:", potential_names_filename, "containing list of names has not been found.")
    except (ValueError):
        print("no_of_people too large. Must be <= to the number of names in file:", potential_names_filename)
    except AssertionError as error:
        print(error)
        

if __name__ == "__main__": 
	main() 