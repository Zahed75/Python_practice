# print the second value
fruits = ["apple", "mango", "litchi"]
print(fruits[1])

# change the value from apple to the litchi

fruits = ["apple", "mango", "litchi"]

fruits[0] = "litchi"
print(fruits)

# use to the append method to add orange

fruits = ["apple", "banana", "mango", "litchi"]

fruits.append("orange")

print(fruits)

# Use the insert method to add "lemon" as the second item in the fruits list.

f = ["apple", "banana", "cherry"]
f.insert(1, "lemon")

print(f)

#Use the remove method to remove "banana" from the fruits list.


fruits = ["apple", "banana", "cherry"]
fruits.remove("banana")
print(fruits)

#Use negative indexing to print the last item in the list.


fruits = ["apple", "banana", "cherry"]
print(fruits[-1])

#Use a range of indexes to print the third, fourth, and fifth item in the list.


fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(fruits[2:5])

#Use the correct syntax to print the number of items in the list.


fruits = ["apple", "banana", "cherry"]
print(len(fruits))