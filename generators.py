# Gnerators are functions that return an object that can be iterated over
# They generate the items inside the object lazily (one at the time), just when you ask for it
# More memory efficient when you have to deal with large data sets

import sys

def my_generator():
    yield 5
    yield 2
    yield 3

gene = my_generator()

print(sum(gene))

gene = my_generator()
sorted_gene = sorted(gene)

print(sorted_gene)


g = my_generator()
value = next(g)
print(value)

value = next(g)
print(value)

value = next(g)
print(value)

try:
    value = next(g)
    print(value)
except:
    print("Raise STOP iteration")


def count_down(num):
    print('Starting')
    while num > 0:
        yield num
        num -= 1

cd = count_down(5)

value = next(cd)
print(value)

value = next(cd)
print(value)


# Generator are memory efficient. Follows an example:

def firstn(n):
    nums = []
    num = 1
    while num < n:
        nums.append(num)
        num += 1
    return nums

print(firstn(10))
print(sum(firstn(10)))

# I do not need to create an array of size n.
# generators just iterate over the elements without any extra space
def firstn_generator(n):
    num = 0
    while num < n:
        yield num
        num += 1

print(sum(firstn_generator(10)))

print(sys.getsizeof(firstn(1000000)))
print(sys.getsizeof(firstn_generator(1000000)))

# Generator expression
my_generator = (i for i in range(10) if i%2 == 0)

# List expression
my_list = [i for i in range(10) if i%2 == 0]

print(my_list)

print(next(my_generator))
print(next(my_generator))
print(next(my_generator))
print(next(my_generator))



