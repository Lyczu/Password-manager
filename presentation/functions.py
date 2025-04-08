def myfunc(a):
    """Documentation of func"""
    print(f"Hello, {a}")


### Proste dekoratory 

def make_pretty(func):
    def inner():
        print("I got decorated")
        func()
    return inner

@make_pretty
def ordinary():
    print("I am ordinary")

ordinary() # I got decorated I am ordinary


# Closures + decorators 

def embigger(func):
    embigger = 2
    def inner(a, b):
        return func(a, b) + embigger
    print(inner) # <function embigger.<locals>.inner at 0x790bb07bdee0>
    return inner

@embigger
def adder(a, b):
    return a + b
print(adder) # <function embigger.<locals>.inner at 0x790bb07bdee0>
# Po udekorowaniu adder i inner to to samo -> 0x790bb07bdee0

print(adder(1,2)) # 5

### Dekorator z przekazaniem argumentu

def make_bigger(scalar):
    """ Increases a number """
    def decorator(func):
        def inner(*args, **kwargs):
            return func(*args, **kwargs) + scalar
        return inner
    return decorator

@make_bigger(100)
def add_many(*args):
    sum = 0
    for number in args:
        sum += number
    return sum

# Najpierw wykonywany jest (100), i zwracany dekorator
# Zmienna scalar zostaje zapamiętana (closure)
# Zwracana jest funkcja decorator i to co wyżek

add_many(1,2,3,4,5) # 115

### Dekorator "syntax", czyli jak powinien wyglądac dekorator:

import functools

def em_bigger(x):
    """
    A decorator that adds 'x' to the result of the function.
    """
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            result += x
            return result
        return wrapper
    return decorator

@em_bigger(5)
def add(a, b):
    """Adds two ints"""
    return a + b 

print(add.__name__) # add
print(add.__doc__) # Adds two ints

### Dekorator jako klasa

class Power():
    def __init__(self, arg):
        self._arg = arg
    def __call__(self, a, b):
        retval = self._arg(a, b)
        return retval ** 2
@Power
def subtract(a, b):
    return a-b

print(type(subtract)) # <class '__main__.Power'>
print(subtract(4,1))



def add_repr(cls):
    @classmethod
    def __repr__(cls):
        return f"Hello {cls.__name__}"
    cls.__repr__ = __repr__
    return cls

@add_repr
class User:
    pass

print(User())  # "Hello User"


class InterfaceChecker(type):
    def __new__(cls, name, bases, dct):
        print(name)
        print(bases)
        print(dct)
        #Job
        #()
        #{'__module__': '__main__', '__qualname__': 'Job', 'run': <function Job.run at 0x732d0487e660>}
        if 'run' not in dct:
            raise TypeError("Klasa musi mieć metodę run")
        return super().__new__(cls, name, bases, dct)


class Job(metaclass=InterfaceChecker):
    def run(self):
        print("Running")

