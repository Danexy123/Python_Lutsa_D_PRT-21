import json


class Student:
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

    def load_from_json(self, filename):
        with open('Person.json') as file:
            data_student = json.load(file)

        print(data_student)

name = input("Name: ")
age = input("Age: ")
w = Person(name, age)
w.save_to_json("Person.json")
