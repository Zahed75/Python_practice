# =======List
friend = ["Nila", "shila", "Rakib", "maruf", "Thania"]

bestfriend = ["shihab", "baset vai", "promi", "mitul", "ratul vai", "dabir vai", "badal vai"]

print(friend)

print(bestfriend)

# =====Access the iteam in list

print(bestfriend[1])

# ======Negative Indexing

bazar = ["alu", "potol", "beans", "papya", "tomatoo"]

print(bazar[-1])

# == show the range value

foods = ["pizza", "sandwitch", "burger", "pasta", "pudding", "friedrice", "noodles"]

print(foods[2:5])

# Change Item Value
# To change the value of a specific item, refer to the index number:

fruitslist = ["banana", "orange", "lemon", "pineapple", "guava", "drgaonfruits"]

fruitslist[1] = "watermelon"

print(fruitslist)

# loop through a list

choclate = ["kvendish", "richo", "kitkat", "blueberry"]

for x in choclate:
    print(x)

p_l = ["java", "python", "C++", "C#", ".net", "ruby"]

for n in p_l:
    print(n)

# looping list print serially
choclate = ['kitkat', 'oreo', 'asdf', 'adsfsad']

for i in range(len(choclate)):
    print(i + 1, "." + choclate[i])

#     Check if Item Exists
# To determine if a specified item is present in a list use the in keyword:
name = ["zahed", "hate", "everything", "hate u "]

if "zahed" in name:
    print("please die")

# how to find list length using len function

foods = ["pizza", "pie cake", "sandeich", "hotdog"]
print(len(foods))

# add iteam using append function end of list

st_name = ["ekleel", "sumiaya", "sadia", "keya", "abrar", "mitul"]
st_name.append("kazmi")

print(st_name)

# how to add iteam specified index using inserta function

hobby = ["reading", "playing guitar", "cycling", "sketting", "fishing"]

hobby.insert(1, "coding")

print(hobby)

# how to remove any element from list

# The remove() method removes the specified item:

hobby = ["reading", "playing guitar", "cycling", "sketting", "fishing"]

hobby.remove("playing guitar")

print(hobby)

fvrt_person = ["Baset", "ammu", "abbu", "shihab", "promi", "elen"]

fvrt_person.pop(2)
print(fvrt_person)

# delete specifiy index or elemnt using delete fun
fvrt_person = ["Baset", "ammu", "abbu", "shihab", "promi", "elen"]
del fvrt_person[4]

print(fvrt_person)

# get error because u deleted all the list
# fvrt_person =["Baset","ammu","abbu","shihab","promi","elen"]
# del fvrt_person[]

# print(fvrt_person)

sub_name = ["ElC", "java", "DC", "AC"]

sub_name.clear()
print(sub_name)

# how to copy one list iteam to another list iteam

thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

number = ["3223", "2343", "2343245", "2343323", "235556"]

indexnum = number.copy()

print(indexnum)

# join two list

list1 = ["a", "b", "c", "d"]

list2 = ["e", "f", "g", "h"]

list3 = list1 + list2
print(list3)

# how to add list iteam using append function

list2 = ["A", "B", "C", "D", "E"]
list4 = ["1","2","4","5"]
for x in list4:
    list2.append(x)
print(list2)


#how to extend two list

name = ["zahed","abdul","satyam","mitul"]
l_name = ["hasan","baset","talkudar","hasan"]

name.extend(l_name)
print(name)

#how to add first list iteam sequenitally second list iteam using append func
a = ['zahed', 'shuvro', 'ratul']
b = ['hasan', 'baset', 'anik']
c = []
for i in range(len(a)):
    temp = a[i] + " " +  b[i]
    c.append(temp)
print(c)