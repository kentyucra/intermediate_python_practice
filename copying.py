# use copy module for deep copies
import copy

org = 5

# New variable with the same reference
cpy = org

# now cpy points to a new space in memory with a value of 7
cpy = 7

print(cpy)
print(org)

org_list = [0,1,2,3]

# copy just do a copy in one level (swallow copy)
cpy_lit = copy.copy(org_list)

cpy_lit[0] = -100

# Both are equals
print(org_list)
print(cpy_lit)


original = [[1,2,3], [2,3,4]]
# In order to do copy in all level use "copy.deepcopy"
copy_ori = copy.deepcopy(original)

copy_ori[0][0] = -232

print(original)
print(copy_ori)

# deepcopy can be also be used for custom objects

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Company:
    def __init__(self, boss, employee):
        self.boss = boss
        self.employee = employee

p1 = Person('Alex', 33)
p2 = Person('Kent', 22)

company = Company(p1, p2)
# use deepcopy for copy all the object in all levels
copy_company = copy.deepcopy(company)

copy_company.boss.age = 12

print(copy_company.boss.age)
print(company.boss.age)

