import csv
with open(' demo.csv', 'w') as file:
 writer1 = csv.writer(file)
 writer1.writerow(["SN", "name", "ac number"])
 writer1.writerow([1, "msd", "54677"])
 writer1.writerow([2, "virat", "54326"])
