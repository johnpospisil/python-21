# Python has a module specifically for converting JSON data to Python dictionary,
# and vice versa.

import json

person = {
    "firstName": "Ricky",
    "lastName": "Lickity",
    "titles": [
        "master chef",
        "baker",
        "sushi chef"
    ],
    "hasKids": False,
    "favoriteColor": "gold",
    "ownsRestaurant": True,
    "favoriteNumber": 123,
    "object": {
        "a": "b",
        "c": "d"
    },
    "about": "Master chef with 18 years of exerience. Owner of 'Chez Bastarde'."
}

# convert a dictionary to json format - called serialization or encoding
personJSON = json.dumps(person, indent=4, sort_keys=True)
print(f'\nPython dict converted to JSON format:\n{personJSON}')


# convert a dictionary to json format, and 'write' contents to a file named 'person.json'
with open('person.json', 'w') as file:
    json.dump(person, file, indent=4)


# convert json to a Python dictionary - called deserialization or decoding
person2 = json.loads(personJSON)
print(f'\nJSON data converted to Python dict:\n\n{person2}')
