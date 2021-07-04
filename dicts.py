# Dictionary: Key-Value pairs, Unordered, Mutable
mydict = {
    "name": "Max",
    "age": 28,
    "city": "New York",
}

print(mydict)

mydict2 = dict(name="Mary", age=27, city="Boston")

print(mydict2)

value1 = mydict.get("name")
value2 = mydict["age"]

print(value1)
print(value2)

# Add key-value pair
mydict["email"] = "max@gmail.com"

print(mydict)

# Deleve key-value pair
del mydict["email"]
# mydict.pop("email")

print(mydict)

if "city" in mydict:
    print("yes")
else:
    print("no")

try:
    print(mydict["pepe"])
except:
    print("key does not exits")

for key in mydict.keys():
    print(key)

for value in mydict.values():
    print(value)

for key, value in mydict.items():
    print(key, " + ", value)

# create a copy
mydict_cpy = mydict.copy()

# Merge 2 dictionaries
mydict3 = {
    "name":  "Max",
    "age": 28,
    "email": "hola@gmail.com"
}

mydict4 = dict(name="Mary", age=27, city="Boston")

mydict3.update(mydict4)

print(mydict3)

mydict5 = {
    3: 9,
    6: 36,
    9: 81
}

print(mydict5)

mydict6 = {
    (8,7): 15,
    (1,2,3): 6
}

print(mydict6)

# NOTE: Is not possible to use list as key in dicitionaries
