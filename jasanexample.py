import json

# json string

employee = '{"id":"791", "name": "malli", "department":"Ceo"}'

# Convert string to Python dict
employee_dict = json.loads(employee)
print(employee_dict)
print(type(employee_dict))
print("\n")