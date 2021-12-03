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

### Everything is an object
- Throughout this course, we will encounter many data types: integers (`int`), booleans (`bool`), floats (`float`), strings (`str`), lists (`list`), tuples (`tuple`), set (`set`), dictionaries (`dict`), None (`NoneType`)
- We will also see other constructs: operators (`+`, `-`, `==`, `is`, `...`), functions, classes, types
- But the one thing in common with all these things, is that they are all **objects** (instances of classes):
  - `function`s are instances of the class Function
  - `class`es are instances of the class Class
  - `type`s are instances of the Classes Int, Float, String, ...
- This means they all have a *memory address*!! As a consequence:
  - Any object can be **assigned** to a variable ... **including functions**
  - Any object can be **passed** to a function ... **including functions**
  - Any object can be **returned** from a function ... **including functions** 
``` python
def my_func():
  print(I am an object from the python class Function)
```
- `my_func` is the name of the function
- `my_func()` invokes the function
- **`help(int)` will tell you the documentation of the class `int`**

### Python Optimization: `Int` Interning
- A lot of what we discuss with memory managements, garbage collection and optimizations, is usually specific to the Python implementation you use.
- This notes are using CPython, the standard (or reference) Python implementation (written in C)
- But there are other Python implementations out there. These include:
  - **Jython** - written in Java and can import and use any Java class - in fact it even compiles to Java bytecode which can then run in a JVM
  - **IronPython** - this one is written in C# and targets .Net (and mono) CLR
  - **PyPy** - This one is written in RPython (which is itself a statically-typed subset of Python written in C that is specifically designed to write interpreters)
  - Many more -> https://wiki.python.org/main/PythonImplementations
#### Looks the code below, what is going on????
``` python
a = 10
b = 10
id(10) == id(10) # True
a = 500
b = 500
id(a) == id(b) # False
```
- Interning: reusing objects on-demand. At startup, Python (CPython), pre-loads (caches) a global list of integers in the range `[-5, 256]` 
- Any time an integer is referenced in that range, Python will use the cached version of that object.
- **Singletons** Optimization strategy - small integers show up often
- When we write `a = 10` Python just has to point to the existing reference for 10
- But if we write `a = 257` Python does not use that global list and a new object is created every time

### Python Optimization: `String` Interning
- Some strings are also automatically **interned** - but not all!!
- As the python code is compiled, **identifiers** are interned: variable names, function names, class names, etc
- Some string literals may also be automatically interned
  - String literals that look like identifiers (e.g. `'hello_world'`)
  - Although if it starts with a digit, even though that is not a valid identifier, it may still get interned, **but do NOT count on it**
#### Why do this?
- It's all about (speed and, possibly, memory) optimization.
- Python, both internally, and in the code you write, deals with lots and lost of dictionary type lookups, on string keys, which means a lot of **string equality** testing.
- Let's say we want to see if two (longs) string are equal `str_1 == str_2`, we need to compare the two strings **character by character**
- But if we know that `srt1` has been interned, then srt1 and str2 are the same string if they both point to the same memory address
- In which case we can use `str1 is str2` instead - which compares two integers (memory address)
- Not all strings are automatically internted by Python, but you can **force** strings to be interned by using the `sys.intern()` method.
``` python
import sys
str_1 = sys.intern('the quick brown fox')
str_2 = sys.intern('the quick brown fox')
str_1 is str_2 # True
```
- This is much faster than `str_1 == str_2`
- When should you do this?
  - Dealing with a large number of strings that could have high repetition e.g. tokenizing a large corpus of text (NLP)
  - Lots of string comparisons.
- **In general though, you do not need to intern strings yourself. Only do this if you really need to.**

### Python Optimization: Peephole
- This is another variety of optimizations that can occur at compile time
#### Constant expressions
- Numeric calculations (e.g. `24 * 60` --> `1440`)
- Short sequences length < 20
  - `(1, 2) * 5` --> `(1, 2, 1, 2, 1, 2, 1, 2, 1, 2)`
  - `'abc' * 3` --> `'abcabcabc'`
  - `'hello' + ' world'` --> `'hello world'`
#### Membership Tests: Mutables are replaced by inmutables
- When membership test such as `if e in [1, 2, 3]` are encountered, the `[1, 2, 3]` **constant**, is replaced by its inmutable counterpart `(1, 2, 3)` tuple
- List are changed by tuples, and sets are changed by frozensets

## Numeric Types
- Four main types of numbers
  - Boolean truth values `False`, `True` (bool python type)
  - Integer Numbers `0, +-1, +-2, ...` (`int` python type)
  - Rational Numbers `p/q where p,q belong Integer numbres and q != 0` ('fractions.Fraction` python type)
  - Real Numbers `0, -1, 0.1256, 1/2, pi` (`float` and `decimal.Decimal` python type)
  - Complex Numbers `{a + bi | a, b belongs Real numbers}` (`complex` python type) 
# Integers
- Integers does not have a limitation in the maximum number we can save in an object of the type `int`.
- Working with bigger numbers make the operations take more time.
- Integers support all the standard arithmetic operations: addition(`+`), subtraction(`-`), multiplication(`*`), division(`/`), exponents(`**`)
- What is the resulting type of each operation?
  - `int` (`+`, `-`, `*`, or `**`) `int` -> `int`
  - `int / int` -> `float`
- `//` is called **floor division**
- `%` is called the **modulo** operator (mod)
