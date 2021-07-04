from itertools import product, permutations, combinations, accumulate, groupby
# infinite iterators
from itertools import count, cycle, repeat
import operator

b = [3, 4]
a = [1, 2]

prod = product(a, b, repeat=2) # it repeats the multiplication twice = (axb)x(axb) 

print(list(prod))

a = [1,2,3]

# perm = permutations(a) # Create all permutations from a
perm = permutations(a, 2) # Second value will  create all permutation with 2 elements

print(list(perm))

comb = combinations(a, 2) # Second argument is mandatory 

print(list(comb))

a = [1,2,3,4,5]

# accum = accumulate(a) # By default compute the sum
# accum = accumulate(a, func=operator.mul) 
accum = accumulate(a, func=max) 
print(list(accum))

# First example groupby
def smaller_than_3(x):
    return x < 3

a = [34,2,36,5,1]

group_obj = groupby(a, key=lambda x: x < 3)

for key, value in group_obj:
    print(key, list(value))

# Second example groupby
persons = [
    {
        'name': 'Tim',
        'age': 25
    },
    {
        'name': 'Lisa',
        'age': 25
    },
    {
        'name': 'Dan',
        'age': 27
    },
    {
        'name': 'Claire',
        'age': 28
    }
]

group_obj = groupby(persons, key=lambda x: x['age'])
for key, value in group_obj:
    print(key, list(value))

a = [1,2,3,4]
# Start in count and go infinite
for i in count(10):
    print(i)
    if i == 15:
        break

# Cycle infinite over the array a
for i in cycle(a):
    print(i)
