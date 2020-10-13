# Dictionary are changeble ordered indexed etc

info = {
    "name": "Zahed",
            "age": "21",
            "sub":"CSE",
            "year":"2017"
}

print(info)

#accesing the iteam calling the key value

club_info={
    "name":"zahed",
    "department":"CSE",
    "id":"20018"
}

x=club_info["id"]

print(x)

#accesing the iteam calling get method
club_info={
    "name":"zahed",
    "department":"CSE",
    "id":"20018"
}

x=club_info.get("id")

print(x)