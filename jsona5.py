# import module
import json

# Data to be written
data = {
 "user": {
     "name": "Malli",
     "age": 21,
     "Place": "Bangalore",
     "Blood group": "O+"
  }
 }

# Serializing json and
# Writing json file
with open( "datafile.json" , "w" ) as write:
 json.dump( data , write)