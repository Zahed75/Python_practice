name = ("Zahed", "Hasan", "Morsheda", "neela", "nodi")

print(name[1])

print(len(name))

print(name[-3])

fruits = ("Mango", "stawbeery", "Litchi", "Guava", "Banana")

print(fruits[2:4])

print(fruits[2:4])

college = ("DC", "Daffodil", "NDC", "Holy Cross", "UIU")
for x in college:
    print(x)

name = ("zahed", "zahedh", "promi", "neela", "rayhan")
if "zahed" in name:
    print("yes we got the culprit")

foods = ["rice", "pizza", "chicken"]
foods.append("oil")
print(foods)

kichuri = ["rice", "dal", "chicken", "slat"]
kichuri.append("doi")
print(kichuri)

cake = ["egg", "suger", "oil", "falvour", "baking powder", "foodcolor"]
cake.remove("foodcolor")
print(cake)

cake = ["egg", "suger", "oil", "falvour", "baking powder", "foodcolor"]
cake.pop(1)
print(cake)

juice = ["mango", "banana", "strabwerry", "litchi"]
del juice[1]
print(juice)

love = ["friend", "best friend", "janina", "bal", "heda"]

del love

result = ["34", "345", "53", "3423", "767", "23", "234"]
result.clear()
print(result)

test = ["bio", "che", "physics", "math", "IOT"]
test2 = test.copy()
print(test2)

moive_name = ["50shades", "hollow men", "battle royle", "heda", "bal"]

release = list(moive_name)
print(release[2])

name = ["zahed", "pormi", "lucifer", "backdoor"]
age = ["22", "23", "33", "4343"]
pack = name + age
print(pack)

name = ["zahed", "pormi", "lucifer", "backdoor"]
age = ["22", "23", "33", "4343"]

for x in age:
    name.append(x)
print(name)

hate = ["cloning", "reversing", "switching"]
pot = ["rock", "aket", "run"]
for x in pot:
    hate.extend(x)
print(hate)

name=list(("Zahed","sabbir","siam","arnob"))
print(name)