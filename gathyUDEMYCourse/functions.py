# # FUNCTIONS
#
# def my_first_function():
#     "This is our first function!"
#     print("Hello Python!")
#
#
# # help(my_first_function())
#
# my_first_function()
#
#
# def my_first_function():
#     print("Hello Java!")
#
#
# my_first_function()
#
#
# def my_first_function(x):
#     print(x)
#
#
# my_first_function("Hello World")
#
#
# def my_second_function(x, y):
#     print("Hello " + x)
#     print("Hello " + y)
#
#
# my_second_function("Python", "Java")
#
#
# def my_sum(x, y):
#     sum = x + y
#     return sum
#
# print(my_sum(1, 2))
#
#
# def my_sum(x, y, z):
#     sum = (x + y) * z
#     return sum ** 2
#
# print(my_sum(1, 2, 3))
#
# # ARGUMENTS
#
# # *args is an empty tuple at first but can be filled with other arguements for the function
# def function1(x, *args):
#     print(x)
#     print(args)
#
# function1("hello")
#
# function1('hello', 100, 200)
#
# def function1(x, *args):
#     print(x)
#     for argument in args:
#         print(argument)
#
# function1(1, 2, 3)
#
# # NAMESPACES container holding the names we define where each name is associated with the name space it is defined in
# # built in, global, and local namespaces
#
# print(list(range(10)))
#
# # my_var = 10
# # print(my_var)
#
# def my_var_function():
#     my_var = 10
#     print(my_var)
#
# my_var_function()
# # print(my_var * 10) wont work because now my_var is limited to being inside the function and is not global
#
# my_var = 5
# def my_var_function():
#     global my_var
#     print(my_var)
#
# my_var_function()
#
# def my_var_function():
#     my_var = 10
#     print(my_var)
#     return my_var
#
# result = my_var_function()
#
# print(result * 10)

# MODULES

import math
print(dir(math))
print(math.pi)

import sys
print(dir(sys))
print(help(sys))