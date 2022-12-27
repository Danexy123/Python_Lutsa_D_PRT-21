import json


class Student:
    def __init__(self, name, age, group, acad_perf, ):
        self.name = name
        self.age = age
        self.group = group
        self.acad_perf = acad_perf

    def save_to_json(self, filename):
        data = {
            "name": self.name,
            "aga": self.age,
            "group": self.group,
            "academic performance": self.acad_perf
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
