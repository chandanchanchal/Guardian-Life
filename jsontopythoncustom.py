import json
from collections import namedtuple
from json import JSONEncoder

def movieJsonDecod(movieDict):
    return namedtuple('X', movieDict.keys())(*movieDict.values())

# class for your reference
class Movie:
    def __init__(self, name, year, income):
        self.name = name
        self.year = year
        self.income = income

# Suppose you have this json document.
movieJson = """{
    "name": "Interstellar",
    "year": 2014,
    "income": 7000000
}"""

# Parse JSON into an Movie object
movieObj = json.loads(movieJson, object_hook=movieJsonDecod)
print("After Converting JSON into Movie Object")
print(movieObj.name, movieObj.year, movieObj.income)
