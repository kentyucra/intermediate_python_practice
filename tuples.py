# Tuple: ordered, inmutable, allows duplicate elements
mytuple = ("Max",)
mytuple1 = tuple(["Max", 28, "Boston"])

print(mytuple)

item = mytuple1[2]

print(mytuple1)
print("item: " + item)

# TypeError: 'tuple' object does not support item assignment
# mytuple[0] = "hola"

if 28 in mytuple1:
    print("yes")
else:
    print("no")

mytuple2 = ('a', 'p', 'p', 'l', 'e')

# count number of elements
print(mytuple2.count('p'))

mytuple3 = (1,2,3,4,5,6,7,8,9,10)

slice = mytuple3[2::2]
# reverse tuple 
reverse_tuple = mytuple3[::-1]

print(slice)

mytuple4 = "Max", 28, "Boston"
# number variables should match the number of tuples
name, age, city = mytuple4

print("name: ", name)
print("age: ", age)
print("city: ", city)

mytuple5 = (0,1,2,3,4)

i1, *i2, i3 = mytuple5

print(i1)
print(i2)
print(i3)

# Working with tuples could be more efficient than working with Lists
