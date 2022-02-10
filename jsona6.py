import json

# Data to be written
data = {
  "user": {
    "name": "msd",
     "age": 21,
     "Place": "Hyderabad",
     "Blood group": "B+"
  }
 }

# Serializing json
res = json.dumps( data )
print( res )
