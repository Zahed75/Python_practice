# Associative array

# dict = {
#     "name": "Zahed",
#     "id": "534985",
#     "major": "CSE"
# }
#
# x = dict.values()
# y = dict.keys()
# print(x, y)
# print(dict["name"])
# del dict["major"]
# print(dict)
#
#
#
# dict1 = {
#     "name": "Zahed",
#     "id": "534985",
#     "major": "CSE"
# }
#
# dict1["phn"]="01611871"
# print("update",dict1)
#
#
# #add values in dictionary
#
# stdnt_info={
#     "name":"zahed",
#     "major":"cse",
#     "city":"dhaka"
# }
#
# print(stdnt_info)
#
# #update values
# stdnt_info["contact"]="023452154"
# print("update details",stdnt_info)
#
# # Python program to add a key:value pair to dictionary
#
# dict = {'key1': 'geeks', 'key2': 'for'}
# print("Current Dict is: ", dict)

# using the subscript notation
# Dictionary_Name[New_Key_Name] = New_Key_Value

# dict['key3'] = 'Geeks'
# dict['key4'] = 'is'
# dict['key5'] = 'portal'
# dict['key6'] = 'Computer'
# print("Updated Dict is: ", dict)

#add to dictionary

dict1={
    "key":"zahed","key2":"Dhaka","key3":"897893245"
}

dict2={
    "major":"cse","cont":"9834","B.GRP":"B+"
}

dict1.update(dict2)
print(dict1)

#ittearte
school={
    "name":"Khan International",
    "Class":"grade_1",
    "contact":"5454"
}
#key print
for a in school:
    print(a)
#values show
for i in school:
    print(school[i])

for x in school:
    print(x)
    print(school[x])

for x in range(0,5):
    print(x)

#print even numder

for x in range(0,51,2):
    print(x)