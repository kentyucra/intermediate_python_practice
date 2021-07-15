
import functools
from typing import ItemsView

# Syntax of a decorator
# @mydecorator
# def dosomething():
#     pass

def start_end_decorator(func):
    def wrapper():
        print('Start')
        func()
        print('End')
    return wrapper

def print_name():
    print("Kent Yucra")

# Essence of a decorator without using a decorator
start_end_deco_print_name = start_end_decorator(print_name)

start_end_deco_print_name()

@start_end_decorator
def print_name_with_decorator():
    print("Kent Quispe")

print_name_with_decorator()

# Decorator with funcitons with arguments
def start_end_decorator_with_arguments(func):

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print('start')
        result = func(*args, **kwargs)
        print('end')
        return result
    return wrapper

@start_end_decorator_with_arguments
def adds(x):
    return x+5

print(adds.__name__)

# NOTE: This is a template for every function decorator
# we want to create
def my_decorator(func):

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Do something before
        result = func(*args, **kwargs)
        # Do something after
        return result
    return wrapper


# Decorator that accept arguments
def repeat(num_times):
    def decorator_repeat(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator_repeat


@repeat(num_times=3)
def greet(name):
    print(f"hello {name}")

greet("kent")

def debug(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f"{k} = {v!r}" for k, v in kwargs.items()]
        signature = ','.join(args_repr + kwargs_repr)
        print(f"Calling {func.__name__}({signature})")
        result = func(*args, **kwargs)
        print(f"{func.__name__!r} returned {result!r}")
        return result
    return wrapper

@debug
@start_end_decorator_with_arguments
def say_hello(name):
    greeting = "Hello" + " " + name
    print(greeting)
    return greeting

say_hello('Alex')

# You can create a class decorator if you want to update 
# a state everytime a function is called with a decorator

class CountCalls:

    def __init__(self, func):
        self.func = func
        self.num_calls = 0
    
    def __call__(self, *args, **kwargs):
        self.num_calls += 1
        print(f"This is executed {self.num_calls} times")
        return self.func(*args, **kwargs)


@CountCalls
def say_hello():
    print('Hello')


say_hello()
say_hello()
say_hello()
say_hello()
