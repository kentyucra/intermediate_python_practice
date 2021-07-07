# Generate pseudo random numbers
import random

# Generate random float number between 0 and 1
a = random.random()
print(a)

# Generate a random float number between a and b
b = random.uniform(a=5, b=10)

print(b)

# Generate a random integer number between a and b
# Upper bound include
c = random.randint(a=5, b=10)

print(c)

# Upper bound NOT include
d = random.randrange(5, 10)

print(d)

my_list = list("ABCDEFG")

# Choice randomly a elemnt from my_list
a = random.choice(my_list)

print(a)

# Pick 3 distinct elements randomly from my_list
b = random.sample(my_list, 3)

print(b)

# Pick 3 NO distinc elements randomly from my_list
c = random.choices(my_list, k=3)

print(c)

# Suffle list in place
random.shuffle(my_list)

print(my_list)

# Generating 1
random.seed(1)
print(random.random())
print(random.randint(1,10))

# Generating 2
random.seed(2)
print(random.random())
print(random.randint(1,10))

# NOTE: Generating 1 is EQUAL to Generating 2
# NOTE: All generated random values with the same seed will be the same
# NOTE: Is not recomended to use those number for security purposes,
# use 'secrets' module instead


import secrets

# Generate a random integer in the range of 1 and 10, 10 not included.
a = secrets.randbelow(10)

print(a)

# Gnerate a number with k random bits (bitwise)
b = secrets.randbits(4)

print(b)

my_list = list("ABCDEGASDASD")

a = secrets.choice(my_list)

print(a)

# NOTE: Secrets module has only 4 methods, in order to work with array and randomness
# works with numpy

import numpy as np

# According to the number of parameters (N) passsd to rand
# it will create a Matrix of dimension N
a = np.random.rand(3,3)

print(a)

# Create an array of integer in the range from 1, 10, 10 excluded
# it create an array of dimension 2 (3x3)
b = np.random.randint(0,10, (3,3))

print(b)

arr = np.array([[1,2,3],[4,5,6],[7,8,9]])
np.random.shuffle(arr)

print(arr)

