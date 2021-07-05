# lambda arguments: expression
# Lambda is one line function
# map(function, seq/list)
# filter(function, seq/list)
# reduce(function, seq/list)

from functools import reduce

add10 = lambda x: x+10

print(add10(45))

mult = lambda x,y: x*y

print(mult(10,6))

points2D = [(1,2), (15,1), (5,-1), (10,4)]
# this sorted in the follow way: (x_1,y_1) < (x_2, y_2) 
points2D_sorted = sorted(points2D)

# the follow sorted wil sorted by the second value y_i
points2D_sorted = sorted(points2D, key=lambda x: x[1])


a = [1, 2, 3, 4, 5]
b = map(lambda x: x*2, a)

print(list(b))

c = filter(lambda x: x%2==0, a)
# equivalent that filter
c = [x for x in a if x%2==0]

print(list(c))

# compute the product of all elements in a
d = reduce(lambda x,y: x*y, a)

print(d)



