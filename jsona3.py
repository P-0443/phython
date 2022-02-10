import json

person_string = '{"name": "Malli", "languages": "English", "numbers": [7, 4.4, null]}'

# Getting dictionary
person_dict = json.loads(person_string)

# Pretty Printing JSON string back
print(json.dumps(person_dict, indent = 4))


# Python program to update JSON
# import json

# JSON data:
x = '{ "organization":"JKTECH","city":"Bangalore","country":"India"}'

# python object to be appended
y = {"pin":523305}

# parsing JSON string:
z = json.loads(x)

# appending the data
z.update(y)

# the result is a JSON string:
print(json.dumps(z))