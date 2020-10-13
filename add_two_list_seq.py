# how to add first list iteam sequenitally second list iteam using append func
a = ['zahed', 'shuvro', 'ratul']
b = ['hasan', 'baset', 'anik']
c = []
for i in range(len(a)):
    temp = a[i] + " " + b[i]
    c.append(temp)
print(c)