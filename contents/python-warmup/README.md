# Get Familiar with Python

- [Get Familiar with Python](#get-familiar-with-python)
  - [Functions](#functions)
  - [Classes](#classes)
  - [Modules & Packages](#modules--packages)
  - [Generators](#generators)
  - [Inheritance and Polymorphism](#inheritance-and-polymorphism)
  - [Decorators](#decorators)
  - [Python Virtual Environments](#python-virtual-environments)
  - [What to do next?](#what-to-do-next)

## Functions 

A user-defined function object is created by a function definition (`def`).

It should be called with an argument list containing the same number of items as the function’s formal parameter list.

``` py
# function​
def get_weather_info():​
    pass​

​# functino with input argument
def kill_process(pid):​
    pass​

​# functino with args and kwargs
def update_model(model, *args, **kwargs):​
    pass​

​# one line function
lambda x, y, z: round((x / y) ** z, 2)
```

## Classes

Classes provide a means of bundling data and functionality together.

- Creating a new class creates a new type of object, allowing new instances of that type to be made.
- Each class instance can have attributes attached to it for maintaining its state.
- Class instances can also have methods (defined by its class) for modifying its state.

``` py
# class​
class NLPException(Exception):​
    pass​

​# class with functions
class Processing:​

    def clean_stop_words(self):​
        pass​

    def clean_rare_words(self, rare_words_list):​
        pass​
```
## Modules & Packages

Import function and use in another file.

``` py
from module1 import greeting

greeting('Metin')
# Hello, Metin!
```
## Generators

A function or method which uses the `yield` statement is called a generator function. Such a function, when called, always returns an iterator object which can be used to execute the body of the function.

Generators are a simple and powerful tool for creating iterators. Below example shows that they can be easy to create.

``` py
def get_fruit1():
    items = ['apple', 'peach', 'pineapple']

    for item in items:
        return item
        
def get_fruit2():
    items = ['apple', 'peach', 'pineapple']

    for item in items:
        print('Current item: ', item, 'Items list: ', items)
        yield item
        print('Going next...')
```

## Inheritance and Polymorphism

A class with some functions.

``` py
class Person:​
    def __init__(self, fname, lname):​
        self.firstname = fname​
        self.lastname = lname​
​
    def printname(self):​
        print(self.firstname, self.lastname)
```

Another class inherits `Person` class.

``` py
class Student(Person):​
    pass​
```

Inheriting class (`Student`) now also has `printname` function, even tough it is defined in inherited class (`Person`).

``` py
x = Student("Mike", "Olsen")​
x.printname()​
```

## Decorators

Decorators wrap a function, **modifying** its behavior.

Simple example for decorators.

``` py
import time 
import math 

def calculate_time(func): 
    def inner1(*args, **kwargs): 
        begin = time.time() 
        func(*args, **kwargs) 
        end = time.time() 
        print("Total time taken in : ", func.__name__, end - begin) 

    return inner1 


@calculate_time
def factorial1(num): 
	time.sleep(2) 
	print('factoria1: ', math.factorial(num)) 


def factorial2(num): 
	time.sleep(2) 
	print('factoria2: ', math.factorial(num)) 


print('Method 1: Sugar syntax')
# sugar syntax!
factorial1(10)

print('Method 2: Sugar syntax')
# long way
calculate_time(factorial2(10))
```

Decorators can really be useful. For example, below case, where a data class needs to be defined. 

``` py
from dataclasses import dataclass

class Student:
    name: str
    lastname: str 
    age: int = None
    gpa: float = None
    
    def __init__(self, name='Mike', lastname='Olsen'):
       self.name = name
       self.lastname = lastname


@dataclass
class Student:
    name: str 
    lastname: str 
    age: int = None
    gpa: float = None
```

## Python Virtual Environments

Environment is a container for your application to run isolated with safely and without interrupting any other existing applications in the same machine.

There are many virtual environment tools, but I will be listing some of the well known ones.

- [Venv](https://docs.python.org/3/library/venv.html#module-venv), the standard virtual environments package
- [Virtualenv](https://virtualenv.pypa.io/en/latest/), where venv is mostly developed from.
- [Pipenv](https://pipenv.pypa.io/en/latest/), both package manager and environment maintainer using `virtualenv`.
- [Conda](https://docs.conda.io/projects/conda/en/latest/), anaconda package manager
- [Poetry](https://python-poetry.org/), package manager

## What to do next?

- Search [GitHub](https://github.com/search?q=python+tutorial) for python tutorials
- [W3School](https://www.w3schools.com/python/default.asp​) 
- More on [decorators](https://realpython.com/primer-on-python-decorators/​)
- [Virtual env vs VirtualEnvWrapper](https://realpython.com/python-virtual-environments-a-primer/)