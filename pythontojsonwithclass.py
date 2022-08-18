import json
from json import JSONEncoder

class Student(object):
    def __init__(self, rollNumber, name, *args, **kwargs):
        self.rollNumber = rollNumber
        self.name = name

class StudentEncoder(JSONEncoder):
        def default(self, o):
            return o.__dict__

student = Student(1, "Emma")

# encode Object it
studentJson = json.dumps(student, cls=StudentEncoder, indent=4)

#Deconde JSON
resultDict = json.loads(studentJson)

print("Converting JSON into Python Object")
studentObj = Student(**resultDict)

print("Object type is: ", type(studentObj))

print("Student Details")
print(studentObj.rollNumber, studentObj.name)
