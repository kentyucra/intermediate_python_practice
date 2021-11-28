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

