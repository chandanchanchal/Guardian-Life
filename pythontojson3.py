import json

class Employee(dict):
    def __init__(self, name, age, salary, address):
        dict.__init__(self, name=name, age=age, salary=salary, address=address)

class Address(dict):
    def __init__(self, city, street, pin):
        dict.__init__(self, city=city, street=street, pin=pin)

address = Address("Alpharetta", "7258 Spring Street", "30004")
employee = Employee("John", 36, 9000, address)

print("Encode into JSON formatted Data")
employeeJSON = json.dumps(employee)
print(employeeJSON)

# Let's load it using the load method to check if we can decode it or not.
print("Decode JSON formatted Data")
employeeJSONData = json.loads(employeeJSON)
print(employeeJSONData)
