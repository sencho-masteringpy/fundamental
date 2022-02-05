# key dict must string
# dictionary == json == restAPI

user = {
    "id": 1,
    "premium": True,
    "name": "Agus",
    "username": "AgusTjakep",
    "email": "agusgantenx@gmail.com",
    "adrees": {
        "kota": "diatas langit",
        "desa": "konoha",
        "rt": 4,
        "geo": {
            "lat": "-37.3159",
            "lng": "81.1496"
        }
    }
}

print(user)
print(type(user))
print(user["premium"])
print(user["adrees"]["desa"])
print(user["adrees"]["geo"]["lat"])

# change from dictionary to json format
import json
result = json.dumps(user)
print(result)
print(type(result))

# create and open json files with open syntax
with open('result.json', 'w') as file:
    json.dump(user, file)