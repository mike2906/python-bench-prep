from typing import List

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_json(cls, data):
        return cls(**data)

    def __eq__(self, other):
        return self.name == other.name and self.age == other.age

    def __repr__(self):
        return f"{self.name} is {self.age} years old."

class People(object):
    def __init__(self, people: List[Person]):
        self.people = people

    @classmethod
    def from_json(cls, data):
        people = list(map(Person.from_json, data["people"]))
        return cls(people)
    
    def __eq__(self, other):
        return self.people == other.people

