import json

# list conversion to Array
print(json.dumps(['Welcome', "to", "JK tech"]))

# tuple conversion to Array
print(json.dumps(("jk tech", "imagine", "the", "future")))

# string conversion to String
print(json.dumps("malli"))

# int conversion to Number
print(json.dumps(791))

# float conversion to Number
print(json.dumps(58.443))

# Boolean conversion to their respective values
print(json.dumps(True))
print(json.dumps(False))

# None value to null
print(json.dumps(None))