# Sets: unordered, mutable, no duplicates
# It is possible to do almost every mathematical operation with sets
myset = {1,2,3,4,1}

print(myset)

myset1 = set([1,2,5,7])

print(myset1)

myset1.add(3)

print(myset1)

# raise an error if element is not present, use discard if you do not want the error
myset1.remove(1)

print(myset1)

for i in myset:
    print(i)

if 1 in myset:
    print("yes")
else:
    print("no")

# Unions and intersections
odds = {1,3,5,7,9}
evens = {0,2,4,6,8}
primes = {2,3,5,7}

union = odds.union(evens)

print(union)

intersection = evens.intersection(primes)

print(intersection)

setA = {1,2,3,4,5,6,7,8,9}
setB = {1,2,3,10,11,12}

difference = setA.difference(setB)

print(difference)

setA.update(setB)

print(setA)

myfrozenset = frozenset([1,2,3])

print(myfrozenset)

