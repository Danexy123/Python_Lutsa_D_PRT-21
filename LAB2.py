import json


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def save_to_json(self, filename):
        data = {
            "name": self.name,
            "aga": self.age
        }
        with open(filename, "w") as file:
            json.dump(data, file)

name = input("Name: ")
age = input("Age: ")
w = Person(name, age)
w.save_to_json("Person.json")

with open('Person.json') as f:
    templates = json.load(f)

print(templates)