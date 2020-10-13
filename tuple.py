# # change of tuple values
# x = ("apple", "banana", "cherry")
# y = list(x)
# y[1] = "kiwi"
# x = tuple(y)
#
# print(x)
#
# # Access the iteam value
#
# name = ("Zahed", "Hasan", "Ayat", "elen", "Neela")
#
# print(name[3])
#
# # negative indexing
# name = ("Zahed", "Hasan", "Ayat", "elen", "Neela")
# print(name[-2])
#
# # SLicing negative Indexing
# fruits = ("Apple", "banana", "mango", "cheery", "jackfruit", "litchi", "guava", "star apple")
# print(fruits[-4:-1])
#
# subject = ("math", "chem", "h.math", "biology")
#
# for x in subject:
#     print(subject)

# check iteam in tuple

st_name = ("zahed", "hasan", "tanuja", "shihab", "keya", "robin", "zah", "zad", "tan")

if "zahed"and"zad"and"zah" in st_name:
    print("yes we got it")

#tuple length
st_name = ("zahed", "hasan", "tanuja", "shihab", "keya", "robin", "zah", "zad", "tan")

print(len(st_name))


#Create Tuple With One Item
#To create a tuple with only one item, you have to add a comma after
# the item, otherwise Python will not recognize it as a tuple.

test=("hello",)
print(type(test))

test2=("bengal","bengal","bangladesh") #multiple iteam hole tuple show korbe
print(type(test2))