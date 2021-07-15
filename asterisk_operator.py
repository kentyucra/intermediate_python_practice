"""
Different use cases from the asterisk or star sign in python
- Matematical operations
- Creation of list and tuples with repeated elements
- For args, kwargs
- Unpacking list, container, dicts
- Merging container in lists
"""
# Product
result = 5 * 7

# Power
result = 5 ** 2

print(result)

# Create a list 
zeros_ones = [0,1] * 10 # [0, 1, 0, 1, ..., 0, 1]

zeros_ones = "01" * 10 # "0101010...01"

numbers = [1, 2, 3, 4, 5, 6]

*begining, last = numbers

print(begining) # [1,2,3,4,5]
print(last) # 6

begining, *last = numbers

print(begining) # 1
print(last) # [2,3,4,5,6]

begining, *middle, last = numbers

print(begining) # 1
print(middle) # [2,3,4,5]
print(last) # 6

# merging diferent data types 
my_tuple = (1, 2, 3)
my_list = [4, 5, 6]
my_set = {7, 8, 9}
my_dict_1 = {'a': 1, 'b': 2}
my_dict_2 = {'c': 3, 'd': 4}

new_list = [*my_tuple, *my_list, *my_set]
new_dict = {**my_dict_1, **my_dict_2}

print(new_list)
print(new_dict)


