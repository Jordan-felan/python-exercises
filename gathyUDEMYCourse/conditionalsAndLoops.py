
# CONDITIONALS
x = 100

if x == 5 and type(x) is int:
    print("x equals 5. x is an integer")
    print(x)
elif x == 10 and type(x) is int:
    print("x is an integer but is not equal to 5")

# FOR AND FOR ELSE

# vendors = ["Cisco", "HP", "Nortel", "Avaya", "Juniper"]
#
# for each_vendor in vendors:
#     print(each_vendor)

# my_string = "Cisco"
# for letter in my_string:
#     print(letter)
#     print(letter * 2)
#     print(letter * 3)

# r = range(10)
# for i in r:
#     print(i * 2)


# vendors = ["Cisco", "HP", "Nortel", "Avaya", "Juniper"]
# print(len(vendors))
#
# print(list(range(5)))
#
# for element_index in range(len(vendors)):
#     print(vendors[element_index])
#
# for index, element in enumerate(vendors):
#     print(index, element)
#
# for element in vendors:
#     print(element)
# else:
#     print("the end of the list has been reached")

# WHILE and WHILE ELSE loops

# x = 1
#
# while x <= 10:
#     print(x)
#     x = x + 1
#
# # while True:
# #     do something
#
# while x <= 10:
#     print(x)
#     x = x + 1
# else:
#     print("x is now greater than 10")

# NESTING

# x = "Cisco"
# if "i" in x:
#     if len(x) > 3:
#         print(x, len(x))
#
#
#
# list1 = [4, 5, 6]
#
# list2 = [10, 20, 30]
#
# for i in list1:
#     for j in list2:
#         print(i * j)
#     print(i)

x = 1

# while x <= 10:
#     z = 5
#     x += 1
#     while z <= 10:
#         print(z)
#         z += 1

# for number in range(10):
#     if 5 <= number <= 9:
#         print(number)

# BREAK, CONTINUE, AND PASS
# for number in range(10):
#     if number == 7:
#         break
#     print(number)

# list1 = [4, 5, 6]
#
# list2 = [10, 20, 30]
#
# for i in list1:
#     for j in list2:
#         if j == 20:
#             break
#         print(i * j)
#     print("Outside of the nested loop")
#
# for i in range(10):
#     pass

# TRY, EXCEPT, ELSE, FINALLY

# for i in range(5):
#     try:
#         print(i / 1)
#     except ZeroDivisionError as e:
#         print("Division by 0 is just wrong")
#     except NameError:
#         print("Name error detected")
#     except ValueError:
#         print("Wrong value")

try:
    print(4/2)
except NameError:
    print("Name Error")
else:
    print("No exceptions raised by the try block!")


try:
    print(4/0) #in the "try" clause you insert the code that you think might generate an exception at some point
except ZeroDivisionError:
    print("Division Error!") #specifying what exception types Python should expect as a consequence of running the code inside the "try" block and how to handle them
else:
    print("No exceptions raised by the try block!") #executed if the code inside the "try" block raises NO exceptions
finally:
    print("I don't care if an exception was raised or not!") #executed whether the code inside the "try" block raises an exception or not






