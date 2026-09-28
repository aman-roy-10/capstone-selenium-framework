import json

# Create data
data = {
    "students": [
        {
            "name": "Aman Roy",
            "email": "aman@gmail.com"
        },
        {
            "name": "Rahul Kumar",
            "email": "rahul@gmail.com"
        },
        {
            "name": "Priya Sharma",
            "email": "priya@gmail.com"
        }
    ]
}

# Write data to JSON file
with open("output.json", "w") as file:
    json.dump(data, file, indent=4)

print("JSON file created successfully")