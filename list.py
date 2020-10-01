#=======List
friend = ["Nila","shila","Rakib","maruf","Thania"]

bestfriend = ["shihab","baset vai","promi","mitul","ratul vai","dabir vai","badal vai"]

print(friend)

print(bestfriend)

#=====Access the iteam in list

print(bestfriend[1])

#======Negative Indexing

bazar=["alu","potol","beans","papya","tomatoo"]

print(bazar[-1])

#== show the range value

foods=["pizza","sandwitch","burger","pasta","pudding","friedrice","noodles"]

print(foods[2:5])


# Change Item Value
# To change the value of a specific item, refer to the index number:

fruitslist = ["banana","orange","lemon","pineapple","guava","drgaonfruits"]

fruitslist[1]= "watermelon"

print(fruitslist)

# loop through a list

choclate =["kvendish","richo","kitkat","blueberry"]

for x in choclate:
    print(x)
    
    
p_l=["java","python","C++","C#",".net","ruby"]

for n in p_l:
    print(n)
    
    


#looping list print serially 
choclate = ['kitkat', 'oreo', 'asdf', 'adsfsad']

for i in range(len(choclate)):
    print(i+1,"." + choclate[i])
    
    
    
#     Check if Item Exists
# To determine if a specified item is present in a list use the in keyword:
name =["zahed","hate","everything","hate u "]

if "zahed" in name:
    print("please die")
    
    

#how to find list length using len function

foods =["pizza","pie cake","sandeich","hotdog"]
print(len(foods))
    

