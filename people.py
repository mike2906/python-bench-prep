import sqlalchemy
from typing import List
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from base import Base
from json import JSONEncoder
import json


class Person(Base):
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        """self.__dict__ = {
            'name': self.name,
            'age': self.age
        }"""
    
    __tablename__ = 'people'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)

    def to_json(self):
        return dict(name=self.name, age=self.age)


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
        
    def to_json(self):
        return dict(people=self.people)

    @classmethod
    def from_json(cls, data):
        people = list(map(Person.from_json, data["people"]))
        return cls(people)
    
    def __eq__(self, other):
        return self.people == other.people


class PeopleEncoder(json.JSONEncoder):
    def default(self, obj):
        if hasattr(obj,'to_json'):
            return obj.to_json()
        else:
            return json.JSONEncoder.default(self, obj)