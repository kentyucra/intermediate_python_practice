# Strings: orderd, inmutable, text representation

my_string = "Hello \"World"
# my_string = 'Hello \"World'

# '\' means it should go in the same line
doco1 = """Hello \ 
World
"""

doco2 = """Hello
World
"""

print(doco2)

char = my_string[0]

# Inmutable
# my_string[0] = 'h'

print(char)

substr = my_string[1:5]

# accessing to sustring [x:y:z]
# x start
# y end
# z jumping
# reverse string[::-1]

print(substr)

for i in my_string:
    print(i)

greeting = "Hello"

if "ell" in greeting:
    print("yes")
else:
    print("no")

print(greeting.upper())
print(greeting.lower())

print(greeting.startswith("He"))
print(greeting.endswith("o"))

print(greeting.find("lo"))

print(greeting.count('l'))

print(greeting.replace("He", "HE"))


strings = "How,are,you,doing"

my_list = strings.split(",")

print(my_list)

new_string  = '-'.join(my_list)

print(new_string)


my_list = ['a']*6

# bad, too expensive
my_string = ''
for i in my_list: # O(my_list* my_list)
    my_string += i # it take O(size of mylist)

# good, linear
my_string = ''.join(my_list)


# Format a string
# %, .format(), f-strings

# First method
var = "Tom"
my_string = "the variable is %s" % var
print(my_string)

var = 3
my_string = "the variable is %d" % var
print(my_string)

var = 4.23232323
my_string = "the variable is %.6f" % var
print(my_string)

# Second method
var1 = 3.1312312
var2 = "hola"
my_string = "the variable is {:.2f} and {}".format(var1, var2)
print(my_string)

# Third method
my_string = f"ggola pepe {var1*2}  and {var2}"
print(my_string)

