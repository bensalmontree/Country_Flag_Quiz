import csv
file = open("Country_Flag_Quiz/country_flags.csv", "r")
all_flags = list(csv.reader(file, delimiter=","))
file.close()

# remove the first row (header values)
all_flags.pop(0)

# get the first 50 rows (used to develop colour buttons for play GUI)
print(all_flags[:50])

print("Length: {}".format(len(all_flags)))