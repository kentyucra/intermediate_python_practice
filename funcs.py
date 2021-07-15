"""
- The difference between arguments and parameters
- Positional and keyword arguments
- Default arguments
- Variable-length arguments (*args and **kwargs)
- Container unpacking into function arguments
- Local vs global arguments
- Parameter passing (by value or by reference?)
"""

"""The difference between arguments and parameters"""

# name is a parameter
def print_name(name):
    print(name)

# 'kent' here is a argument
print_name('kent')


"""Positional and keyword arguments"""

def foo(a, b, c):
    print(a, b, c)

# Positional arguments
foo(1, 2, 3)

# Keyword arguments , order is not important
foo(a = 1, c = 3, b = 2)

# Mixed
# NOTE: can not use a positional argument after a keyword argument
foo(1, c = 3, b = 2)

"""Default arguments"""

# d is a default argument
# Default arguments should be go last
# Otherwise the follow syntax error is produce: "non-default argument follow default argument"
def foo(a, b, c, d=4):
    print(a, b, c, d)

"""Variable-length arguments (*args and **kwargs)"""

# args is a tuple
# kwargs is a dictionary
def foo(a, b, *args, **kwargs):
    print(a, b)

    for arg in args:
        print(arg)

    for key in kwargs:
        print(key, kwargs[key])

foo(1,2)
foo(1,2, 3,4,5)
foo(1,2,3,3,4,5, six=6, seven=7)

# Every parameter after * should be a keyword argument
def foo1(a, b, *, c, d):
    print(a,b,c,d)

foo1(1, 2, c=3, d=4)

def foo2(*args, last):
    for arg in args:
        print(arg)
    
    print(last)

foo2(1,2,3,4, last = 5)

"""Container unpacking into function arguments"""

def foo3(a,b,c):
    print(a,b,c)

my_list = [1,2,3]

# Unpacking my_list in a,b,c
# To unpack list and tuples use 1 start (*)
foo3(*my_list)

my_tuple = (1,2,3)

foo3(*my_tuple)

my_dict = {
    'a': 1,
    'b': 2,
    'c': 3
}

# To unpack dictionaries use 2 starts (**) 
# Lenght of dictionary should match the number of parameters
# The names of the parameters should also match
foo3(**my_dict)

"""Local vs global arguments"""

# Function use the global variable number
def foo4():
    # Need to specified which variable you wanna use from the global ones
    global number
    x = number
    number = 3
    print('number inside function:', x)

# Funtions create a local variable, do not use the global one
def foo5():
    number = 3


number = 0
foo4()
print(number)

"""Parameter passing (by value or by reference?)"""
# Mutable objects can be change inside a function (it means the argument is past by reference)
# Inmutable objects can not be change inside a funciton (it means the argument is past by copy) 


# Inmutable
def foo_int(x):
    x = 5

var = 10
foo_int(var)
print(var) # 10

# Mutable
# Rebind (assign a new list) create a local variable and stop working with the arguments passed to the function
def foo_list(a_list):
    # rebind examples
    # a_list = [10,22,45]
    # a_list = a_list + [1,2,3]

    a_list.append(10)
    a_list[0] = -11

my_list = [1,2,3,4]
foo_list(my_list)
print(my_list)




    


 