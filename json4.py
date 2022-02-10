import json
var = {
       "Subjects": {
                   "Maths":85,
                   "English":90
                   }
  }
with open("arraySample.json", "w") as p:
  json.dump(var, p)


# Python program to read
# json  file

# import json

# Opening JSON file
f = open('data.json', 'r')

# returns JSON object as
# a dictionary
data = json.load(f)


# # Iterating through the json
# # list
for i in data['employee']:
    print(i)

# Closing file
f.close()
# Python program to write JSON
# to a file
