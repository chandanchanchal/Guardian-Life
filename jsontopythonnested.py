import json

print("Started reading nested JSON array")
developerDict = json.loads(developerInfo)

print("Project name: ", developerDict["projectinfo"][0]["name"])
print("Experience: ", developerDict["experience"]["python"])

print("Done reading nested JSON Array")
