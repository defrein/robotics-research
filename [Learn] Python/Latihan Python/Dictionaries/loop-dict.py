# Loop through the dictionary

new_dict = {
    "brand": "Honda",
    "model": "Civic",
    "year": 1995
}

# print all key names in the dictionary
for x in new_dict:
    print(x)

# print all values in the dictionary
for x in new_dict:
    print(new_dict[x])

# loop through both keys and values
for x, y in new_dict.items():
    print(x, y)
