import json

# Data to be written
dictionary = {
         "id": "791",
         "name": "Malli",
         "department": "Manager"
        }

with open("data.json", "a") as outfile:
 json.dump(dictionary, outfile)
