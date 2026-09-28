import json

with open("testdata.json", "r") as file:
    data = json.load(file)

for student in data["students"]:
    print("Name:", student["name"])
    print("Email:", student["email"])
    print()