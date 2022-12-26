import json


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def save_to_json(self, filename):
        data = {
            "n": self.name,
            "a": self.age
        }
        with open(filename, "w") as file:
            json.dump(data, file)