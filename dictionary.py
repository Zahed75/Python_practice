# Dictionary are changeble ordered indexed etc

info = {
    "name": "Zahed",
    "age": "21",
    "sub": "CSE",
    "year": "2017"
}

print(info)

# accesing the iteam calling the key value

club_info = {
    "name": "zahed",
    "department": "CSE",
    "id": "20018"
}

x = club_info["id"]

print(x)

# accesing the iteam calling get method
club_info = {
    "name": "zahed",
    "department": "CSE",
    "id": "20018"
}

x = club_info.get("id")

print(x)
# ADD iteam using key method value deeived
CMT = {
    "name": "Zahed",
    "id": "20018",
    "major": "CSE"

}

CMT["major"] = "IOT"
print(CMT)

# loop through in dictionary

fvrt_mam = {
    "name": ["lynza", "rabyea", "yesmin"]
}

for x in fvrt_mam:
    print(x)

# print key value
car = {
    "name": "lamborghini",
    "model": "234234",
    "year": "1997"
}

for x in car:
    print(x)

# print iteam

car = {
    "name": "lamborghini",
    "model": "234234",
    "year": "1997"
}

for x in car:
    print(car[x])

# print dictionray values directly using values method

drone = {
    "model": ["Dji", "mavic", "hex3"],
    "dev": "zahed",
    "year": "3457"

}

for x in drone.values():
    print(x)

# show both values like key and value using iteam method

smstr = {
    "name": "zahed",
    "id": "90943",
    "dep": "cse"
}

for x, y in smstr.items():
    print(x, y)

# key check

smstr = {
    "name": "zahed",
    "id": "90943",
    "dep": "cse"
}

if "dep" in smstr:
    print("yes this in the list")

# find out dictionary lenght

smstr = {
    "name": "zahed",
    "id": "90943",
    "dep": "cse"
}
print(len(smstr))

# add iteam in dictionary

smstr = {
    "name": "zahed",
    "id": "90943",
    "dep": "cse"
}

smstr["age"] = "21"
print(smstr)

#removing iteam using pop method

smstr={
    "name":"zahed",
    "id":"90943",
    "dep":"cse"
}

smstr.pop("dep")
print(smstr)

#remove last key using pop method
# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# thisdict.popitem()
# print(thisdict)


thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

del thisdict["model"]
print(thisdict)

#copy one dictionary to antoher dictionary

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
new =thisdict.copy()
print(new,thisdict)


