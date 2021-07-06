# Errors and Exceptions
# Syntax error vrs exception

# Syntax error
# a = 5 print("hola")
# print(a))

# Type error
# a = 5 + "hola"

# Import error
# import somemodule

# create exception

# x = -5
# if x < 0:
#     raise Exception('x should be positive')

# Good practice to especified the type of error
try:
    a = a + "hola"
except ZeroDivisionError:
    print("blabla")
except Exception as e:
    print("error happens")
    print(e)
else:
    print("everthing is fine")
finally:
    print("cleaning up ...")


class ValueTooHighError(Exception):
    pass

class ValueTooSmallError(Exception):
    def __init__(self, message, value):
        self.message = message
        self.value = value

def test_value(x):
    if x>100:
        raise ValueTooHighError("Too high!!!")
    elif x<5:
        raise ValueTooSmallError("too small", x)

try:
    test_value(1)
except ValueTooHighError as e:
    print(e)
except ValueTooSmallError as e:
    print(e.message, e.value)

