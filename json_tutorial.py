"""
JSON supports primitive types (strings, numbers, boolean), 
as well as nested arrays and objects. 
Simple Python objects are trasnalted to 
JSON according to the following conversion:
python           |       JSON
----------------------------
dict             |    object
list,tuple       |    array
str              |    string
int, long, float |    number
True/False       |  true/false
None             |     null
"""

import json

person = {
    "name": "John",
    "age": 30,
    "city": "New York",
    "hasChildren": False,
    "titles": [
        "engineer",
        "programmer"
    ]
}

# dict to JSON object
personJSON = json.dumps(person, indent=4, sort_keys=True)

print(personJSON)

# dump to a file
# with open('person.json', 'w') as file:
#     json.dump(person, file, indent=4)

# JSON object to dict
person = json.loads(personJSON)

print(person)

with open('person.json', 'r') as file:
    person = json.load(file)
    print(person)


class User:
    def __init__(self, name, age):
        self.name = name
        self.age = name

user = User('Max', 27)

# Custom encoding function
# Encode a custom object
def encode_user(obj):
    if isinstance(obj, User):
        return {
            'name': obj.name,
            'age': obj.age,
            obj.__class__.__name__: True
        }
    else:
        raise TypeError("Object of type User is not JSON serializable")

userJSON = json.dumps(user, default=encode_user)

print(userJSON)

# Other way to encode
from json import JSONEncoder
class UserEnconder(JSONEncoder):

    def default(self, obj):
        if isinstance(obj, User):
            return {
                'name': obj.name,
                'age': obj.age,
                obj.__class__.__name__: True
            }
        return JSONEncoder.default(self,obj)

# Ways to use UserEncoder
userJSON2 = json.dumps(user, cls=UserEnconder)
userJSON3 = UserEnconder().encode(user)

print(userJSON2)
print(userJSON3)



# DECODING

def decode_user(dct):
    if User.__name__ in dct:
        return User(name=dct["name"], age=dct["age"])
    return dct

# decode to a dict, how to decode to User object?
user = json.loads(userJSON)

user_obj = json.loads(userJSON, object_hook=decode_user)



print(user_obj)
