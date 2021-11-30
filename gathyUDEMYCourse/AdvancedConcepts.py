
# ADVANCED CONCEPTS
# LIST, SET, DICTIONARY COMPREHENSIONS
list1 = []

for i in range(10):
    result = i ** 2
    list1.append(result)

print(list1)

list2 = [x ** 2 for x in range(10)]
print(list2)
list3 = [x ** 2 for x in range(10) if x < 5]

set1 = {x ** 2 for x in range(10)}
print(set1)

dict1 = {x : x * 2 for x in range(10)}
print(dict1)

# LAMBDA FUNCTIONS

a = lambda x, y: x * y

print(a(2,10))
print(a(5,10))

def myfunc(mylist):
    list_xy = []
    for x in range(10):
        for y in range(5):
            result = x * y
            list_xy.append(result)
    return list_xy + mylist

print(myfunc([100, 101, 102]))

b = lambda mylist: [x * y for x in range(10) for y in range(5)] + mylist

print(b([100, 101, 102]))

# MAP AND FILTER FUNCTION

def product10(a):
    return a * 10

r1 = range(10)

print(map(product10, r1))

print(list(map(product10, r1)))

print(list(map((lambda a: a * 10), r1)))

print(list(filter((lambda a: a > 5), r1)))

# ITERATORS AND GENERATORS

my_list = [1, 2, 3, 4, 5, 6, 7]

print(my_list)
for element in my_list:
    print(element)

my_iter = iter(my_list)
print(my_iter)
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))

def my_gen(x, y):
    for i in range(x):
        print("i is %d" % i)
        print("y is %d" % y)
        yield i * y

my_object = my_gen(10, 5)
print(next(my_object))
print(next(my_object))
print(next(my_object))
print(next(my_object))
print(next(my_object))
print(next(my_object))
print(next(my_object))
print(next(my_object))
print(next(my_object))
print(next(my_object))

gen_exp =(x for x in range(5))
print(next(gen_exp))
print(next(gen_exp))
print(next(gen_exp))
print(next(gen_exp))
print(next(gen_exp))

# ITERTOOLS
from itertools import *

list1 = [1, 2, 3, 'a', 'b' ,'c']
list2 = [101, 102, 103, 'X', 'Y']

print(chain(list1, list2))
for i in chain(list1, list2):
    print(i)

print(list(chain(list1, list2)))

for i in count(10, 2.5):
    if i <= 50:
        print(i)
    else:
        break

# a = range(11,16)
# for i in cycle(a):
#     if i <= 15:
#         print(i)
#     else:
#         break

filterfalse(lambda x: x < 5, [1, 2, 3, 4, 5, 6, 7])
print(list(filterfalse(lambda x: x < 5, [1, 2, 3, 4, 5, 6, 7])))

print(list(range(10)))

print(list(range(10))[2:9:2])

print(list(islice(range(10), 2, 9, 2)))

# DECORATORS

#Decorators - functions that take another function as a parameter and extend its functionality and behavior without modifying it
def my_decorator(target_function):
    def function_wrapper():
        return "Python is the " + target_function() + " programming language!"
    return function_wrapper

@my_decorator
def target_function():
    return "coolest"

print(target_function())

# THREADING BASICS

import threading
import time

def myfunction():
    print("Start a thread")
    time.sleep(3)
    print("End a thread")

threads = []

for i in range(5):
    th = threading.Thread(target = myfunction)
    th.start()
    threads.append(th)

for th in threads:
    th.join()

for i in range(5):
    myfunction()