import json

with open('Sample.json') as f:
 data = json.load(f)
 print(data)
with open('Sample.json') as f:
   data = json.load(f)

   print(data)

# Python JSON to dict
import json

person = '{"name": "Bob", "languages": ["English", "French"]}'
person_dict = json.loads(person)

# Output: {'name': 'Bob', 'languages': ['English', 'French']}
# print( person_dict)

# Output: ['English', 'French']
print(person_dict['languages'])
