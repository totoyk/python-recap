# print
print('Hello, world!')

# terneary operator
num = 1 + 1
print(num)
print(type(num))

num = 2 / 1
print(num)
print(type(num))

# function
def add(a, b):
    return a + b

print(add(1, 2))
print(type(add(1, 2)))


# class
class Person:
    def __init__(self, name):
        self.name = name

    def say_hello(self):
        print(f'Hello, {self.name}')

p = Person('John')
p.say_hello()


# if else
def check_even_odd(num):
    if num % 2 == 0:
        return 'Even'
    else:
        return 'Odd'

print(check_even_odd(2))
print(check_even_odd(3))

# for loop
def print_numbers_for():
    for i in range(10):
        print(f'for {i}')

print_numbers_for()

# while loop
def print_numbers_while():
    i = 0
    while i < 10:
        print(f'while {i}')
        i += 1

print_numbers_while()

# list
def print_list():
    l = [1, 2, 3, 4, 5]
    for i in l:
        print(f'list {i}')

print_list()

# dictionary
def print_dict():
    d = {
        'a': 1,
        'b': 2,
        'c': 3
    }
    for k, v in d.items():
        print(f'dict {k} {v}')

print_dict()

# set
def print_set():
    s = {1, 2, 3, 4, 5}
    for i in s:
        print(f'set {i}')

print_set()

# tuple
def print_tuple():
    t = (1, 2, 3, 4, 5)
    for i in t:
        print(f'tuple {i}')

print_tuple()

# sample

class Cat:
    def __init__(self, name):
        self.name = name

    def say_hello(self):
        if self.name == 'Fruit':
            print(f'Meow!!, {self.name}')
        else:
            print(f'Meow, {self.name}')

c = Cat('Fruit')
c.say_hello()

c = Cat('Tom')
c.say_hello()
