import json
from collections import namedtuple
from json import JSONEncoder

def customStudentDecoder(studentDict):
    return namedtuple('X', studentDict.keys())(*studentDict.values())

studentJsonData = '{"rollNumber": 1, "name": "Emma"}'


student = json.loads(studentJsonData, object_hook=customStudentDecoder)


print(student.rollNumber, student.name)
