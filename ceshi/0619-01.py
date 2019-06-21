import json

class Student(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

def str2json(std):
    return {
        'name' : std.name,
        'age' : std.age
    }

s = Student('bob', 23)
print(json.dumps(s, default=str2json))

