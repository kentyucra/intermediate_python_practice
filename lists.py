mylist = ["banana", "cherry", "apple"]
print(mylist)

item1 = mylist[0]
item2 = mylist[1]
item3 = mylist[2]

print(item1)
print(item2)
print(item3)


for item in mylist:
    print(item)

if "banana" in mylist:
    print("yes")
else:
    print("no")

mylist.append(11)

print(mylist)

mylist.insert(0,"eooe")
print(mylist)

