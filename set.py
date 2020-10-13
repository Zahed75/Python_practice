#Access Items
#You cannot access items in a set by referring to an index or a key.

#But you can loop through the set items using a for loop, or ask if
# a specified value is present in a set, by using the in keyword.
#sets are unorderd
test={"Zahed","hasan","promi"}
print(test)

fruits={"Mango","Dragon","jackfruit","litchi"}

for x in fruits:
    print(fruits)


fruits={"Mango","Dragon","jackfruit","litchi"}

if "Mango" in fruits:
    print("yes mango on it")

#add iteam in sets using add method
juice={"Mango","wood apple","Litchi","Guava","citcic"}

juice.add("orange")
print(juice)

#add multiple iteam using set iteam
juice={"Mango","wood apple","Litchi","Guava","citcic"}
juice.update(["peanut","blakberry","pineapple"])

print(juice)

#REMOVE AN ITEAM USING REMOVE METHOD

fruits_name={"Apple","mango","banana","blueberry"}
fruits_name.remove("Apple")  #If the item to remove does not exist, remove() will raise an error.
print(fruits_name)

#REMOVE AN ITEAM USING DISCARD METHOD

fruits_name={"Apple","mango","banana","blueberry"}
fruits_name.discard("blueberry")
print(fruits_name)

club={"DTI","DTICT","DIIT","DF"}

x=club.pop()

print(x)

print(club)

