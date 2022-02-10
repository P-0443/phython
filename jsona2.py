
#Convert dict to JSON

import json
person_dict = {'name': 'Mahesh babu',
 'age': 48,
 'children': 3
   }
person_json = json.dumps(person_dict)

Output: {"name": "Mahesh babu", "age": 48, "children": 3}
print(person_json)
# Writing JSON to a file

import json

person_dict = {"name": "Mahesh babu",
 "languages": ["English", "Hindi"],
 "married": True,
 "age": 23
 }

with open('person.txt', 'w') as json_file:
   json.dump(person_dict, json_file)
