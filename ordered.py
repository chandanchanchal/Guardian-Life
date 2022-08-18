import json
from collections import OrderedDict

print("Ordering keys")
OrderedData = json.loads('{"John":1, "Emma": 2, "Ault": 3, "Brian": 4}', object_pairs_hook=OrderedDict)
print("Type: ", type((OrderedData)))
print(OrderedData)
