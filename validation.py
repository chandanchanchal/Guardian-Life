import json

def validateJSON(jsonData):
    try:
        json.loads(jsonData)
    except ValueError as err:
        return False
    return True

InvalidJsonData = """{"name": "jane doe", "salary": 9000, "email": "jane.doe@pynative.com",}"""
isValid = validateJSON(InvalidJsonData)

print("Given JSON string is Valid", isValid)

validJsonData = """{"name": "jane doe", "salary": 9000, "email": "jane.doe@test.com"}"""
isValid = validateJSON(validJsonData)

print("Given JSON string is Valid", isValid)
