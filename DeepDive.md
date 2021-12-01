# Deep dive in Python masterclass
This is a course for python 3.6 (or higher)
## Variable Names
### Must
- Start with underscore (_) or letter (a-z, A-Z)
- Followed by any number of underscores(_), letters (a-z, A-Z), or digits (0-9)
- Ex: `var my_var index1 index_1 _var __var __lt__`
### Can not be reserved words
` None True False and or not if else elif for while brak continue pass def lambda global nonlocal return yield del in is assert class try except finally raise import from with as`
### Conventions
- `_my_var` (single underscore) This is a convention to indicate "internal use" or "private" objects
- `_my_var` Objects named this way will not get imported by a statement such as: `from module import *`
- `__my_var` (double underscore) Used to *mangle* class attributes - useful in inheritance chains
- `__my_var__`(start and finish with double underscore) Used for system-defined names that have a special meaning to the interpreter, **Don't invent them, stick to the ones pre-defined by Python!**
### Other Naming conventions (from the PEP8 Style Guide)
- Package -> shot, all-lowercase names, Preferably no underscores. Ex: `utilities`.
- Modules -> short, all-lowercase names. Can have underscores. Ex: `db_utils dbutils`.
- Class -> CapWords (upper camel case) convention. Ex: `BackAccount`
- Functions -> lowercase, words separated by underscores (snake_case) Ex: `open_account` 
- Variables -> lowercase, words separated by underscores (snake_case) Ex: `account_id`
- Constants -> all-uppercase, words separated by underscores. Ex: `MIN_APR`

## Break, Continue and try Statement 

- **finally** will be execute event when `continue/break` is called, you can use this feature for close a file, database connection and others. 
- `else` statement will be executed after while loop finish without a `break`. An example for this is when we want to find a number inside a array and wanna do something if the number is not there.

``` python
a = 0
b = 2

while a < 4:
  print('---------------------------')
  a += 1
  b -= 1
  
  try:
    a/b
  except ZeroDivisionError:
    print("{0}, {1} - division by 0".format(a, b))
    break # Work also with break
  finally:
    print("{0}, {1} - always excecutes".format(a, b))
  
  print("{0}, {1} - main loop".format(a, b))
else:
  print("Code executed without a zero division error')
```

## The foor loop
- In python, an iterable is an object capable of returning values one at a time.
- If we never hit the `break` else statement will be called in the example below
- `Try`, `catch` and `finally` will work the same as while loop
``` python
for i in range(1, 5):
  print(i)
  if i % 7 == 0:
    print('multiple of 7 found')
    break
else:
  print('No multiple of 7 in the range')
```
- `enumerate(s)` returns a iterable of tuples where the first element is the index and the second element is the value, example below:
``` python
s = 'hello'

for i, c in enumerate(s):
  print(i, c)
```

## Classes
- Getter and setter should be implemented just when we have extra loggic for some property
- Follow an example of a basic class
``` python
class Rectangle:
  def __init__(self, width, height):
    self.width = width
    self.height = height
  
  @property
  def width(self):
    return self._width
  
  @width.setter
  def width(self, width)
    if width <= 0:
      raise ValueError('Width must be positive.')
    else:
      self._width = width
  
  @property
  def height(self)
    return self_height
  
  @height.setter
  def height(self, height)
    if height <= 0:
      raise ValueError('Height must be positive.')
    else:
      self._height = height
  
  # Used for print
  def __str__(self):
    return f"Rectangle: width=${self.width}, height=${height}"
  
  def __repr__(self):
    return f"Rectangle(${self.width}, ${self.height})"
   
  def __eq__(self, other):
    # Make sure we are comparing Rectangles
    if isinstance(other, Rectangle):
      return self.width == other.width and self.height == other.height
    else:
      return false    
```
## Variables and Memory

### Variables are memory references
- `my_var_1 = 10` **references** the object at 0x1000
- `my_var_2 = 'Hello'` **references** the object at 0x1002
- In Python, we can find out the memory address referenced by a variable by using the `id()` function
- This will return a base-10 number, we can convert this base-10 number to hexadecimal, by using the `hex()` function.
### References Counting
- Reference counting is made by the **Python Memory Manager**
- `other_var = my_var`, `other_var` is sharing the reference from `my_var` so *reference count* increase.
- In order to find the reference count we can use `sys.getrefcount(my_var)`. Passing my_var to getrefcount() creates an extra reference!
- `ctypes.c_long.from_address(address).value` does not increase the reference count.
### Garbage Collector
- It is useful when references counting does not free memory. It usually happens when we have a **circular dependency**
- Can be controlled programmatically using the `gc` module, by default it is *turned on*.
- You may turn it **off** if you are **sure** your code does not create circular references - but **beware!!**
- Runs periodically on its own (if turned on). You can call it manually, and even do you own cleanup.
- It does NOT work properly for **Python <3.4**
``` python
import ctypes
import gc

def ref_count(address):
  return ctypes.c_long.from_address(address).value
def object_by_id(object_id):
  for obj in gc.get_objects():
    if id(obj) == object_id:
      return "Object exists"
    return "Not found"

class A:
  def __init__(self):
    self.b = B(self)
    print(f"A: self: {id(self)}, b: {id(self.b)}")

class B:
  def __init__(self, a):
    self.a = a
    print(f"B: self: {id(slef)}, a: {id(self.a)}")

# Disable the garbage collector
gc.disable()

my_var = A()

print('a: \t{0}'.format(hex(id(my_var))))
print('a.b: \t{0}'.format(hex(id(my_var.b))))
print('b.a: \t{0}'.format(hex(id(my_var.b.a))))

# refence counting
print('refcount(a) = {0}'.format(ref_count(a_id)))
print('refcount(b) = {0}'.format(ref_count(b_id)))

# Check if the objects exists for the garbage collector
print('a: {0}'.format(object_by_id(a_id)))
print('b: {0}'.format(object_by_id(b_id)))

my_var = None

# References are for both 1, and reference counting does not free the memory
print('refcount(a) = {0}'.format(ref_count(a_id)))
print('refcount(b) = {0}'.format(ref_count(b_id)))

# Garbage collector does not free the memory because was disable
print('a: {0}'.format(object_by_id(a_id)))
print('b: {0}'.format(object_by_id(b_id)))

# Garbage collector collect
gc.collect()

print('refcount(a) = {0}'.format(ref_count(a_id)))
print('refcount(b) = {0}'.format(ref_count(b_id)))
print('a: {0}'.format(object_by_id(a_id)))
print('b: {0}'.format(object_by_id(b_id)))

# Now there is not objects that garbage collector can find
# And the ref_count will be a no-know number, because that memory was free for the Garbage Collector
```

### Dynamic vs Static Typing
- Some languages (Java, C++, Swift) are *statically* typed.  
- `string myVar = "Hello"` It means we have to specified a **data type** of the variable.
- We can use the built-in `type()` function to determine the type of the object **currently referenced** by a variable
``` python
a = "Hello"
type(a) # str
a = 10
type(a) # int
a = lambda x: x**2
type(a) # function
a = 3 + 4j
type(a) # complex
```

### Variable Re-assigment

``` python
my_var = 10
hex(id(my_var)) # e.g. '0x53d5eaf0`
my_var = 15 # reassignment
hex(id(my_var)) # e.g. '0x53d5eb90'
my_var = my_var + 1
hex(id(my_var)) # e.g. '0x53d5ebb0'
```

- When we reassigned the value of a variable in python, a new object of some type is created (the new value for `my_var`) and the reference of the variable change to that object.
- In fact, the value inside the objects, can never be change.

### Object Mutability
- Consider an object in memory. Changing the data inside the object is called modifying the internal state of the object. 
- **object was mutated:** fancy way to saying the internal data has changed.
- **Mutable** is an object whose interanl state can be changed.
- **Inmutable** is an object whose internal state cannot be changed.

#### Inmutable objects in Python
- Numbers (int, float, booleans, etc)
- Strings
- Tuples
- Frozen sets
- Inmutable User-Defined Classes

#### Mutable objects in Python
- Lists
- Sets
- Dictionaries
- Mutable User-Defined Classes

### Shared References and Mutability
- The term **shared reference** is the concept of two variables referencing to the *same* object in memory (i.e. having the same memory address)
- **With inmutable objects**, Python's memory manager decides to automatically re-use the memory references!! (It does not happens everytime)
``` python
# suprise that id(a) == id(b)
a = 10
b = 10
# the same for another inmutable objects, id(s1) == id(s2)
s1 = 'hello'
s2 = 'hello'
```
- **With mutable objects**, the python manager will never re-use the memory
``` python
# id(a) != id(b)
a = [1, 2, 3]
b = [1, 2, 3]
```

### Variable Equality
- Equiality of **memory address** (if both variables have the same reference - point to the same memory) Use the `is`/`is not` identity operator. i.e. `var_1 is var_2` (*This equility is not reliable*)
- Equality of **object state (data)** (if both variables have the same information) Use the `=`/`!=` equality operator. i.e. `var_1 == var_2` 
### NONE
- The `None` object can be assigned to variables to indicate that they are not set (in the way we would expect them to be), i.e. an "empty" value (or null pointer)
- But the `None` object is a real object that is managed by the Python memory manager
- Furthermore, the memory manager will alway use a shared reference when assigning a variable to None
``` python
a = None
b = None
c = None
id(a) == id(b) == id(c) # True
a is None # True
```
