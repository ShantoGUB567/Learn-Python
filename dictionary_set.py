my_dict = {
    "name": "Shanto",
    "age": 24,
    "city": "Dhaka",
    12 : "twelve"
}

print (my_dict["name"])
print (my_dict[12])
print(my_dict)

print(my_dict.get("city"))

# Functions
print(my_dict.keys())
print(my_dict.values())
print(my_dict.items())

keys = ["name", "age", "city"]
dict = dict.fromkeys(keys, "default")
print(dict)