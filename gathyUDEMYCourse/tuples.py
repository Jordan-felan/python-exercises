#
# # TUPLES
#
# my_tuple = ()
# print(type(my_tuple))
# my_tuple = (9)
# print(type(my_tuple))
# my_tuple = (9,)
# print(type(my_tuple))
# my_tuple = (1, 2, 3, 4, 5)
# print(my_tuple)
# print(my_tuple[0])
# print(my_tuple[1])
# print(my_tuple[-1])
# print(my_tuple[-2])
#
# tuple1 = ("Cisco", "2600", "12.4")
# (vendor, model, ios) = tuple1
# print(vendor)
# print(model)
# print(ios)
# tuple2 = (1, 2, 3, 4)
# (a, b, c) = (10, 20 ,30)
# print(a)
# print(b)
# print(c)
#
# # DIFFERENCE IN TUPLES AND LISTS
# # tuples are immutable and lists are mutable
# # tuple has fixed lengths vs lists have variable lengths
# # tuples enclosed in parentheses while lists are enclosed in square brackets
# # tuple has less available methods and operations than a list
# a = ()
# b = []
# print(type(a))
# print(type(b))
# print(dir(a))
# print(dir(b))

# tuple methods
tuple2 = (1, 2, 3, 4)
print(len(tuple2))
print(min(tuple2))
print(max(tuple2))
print(tuple2 + (5, 6, 7))
print(tuple2 * 2)
print(tuple2[0:2])
print(tuple2[:2])
print(tuple2[1:])
print(tuple2[:])
print(tuple2[:-2])
print(tuple2[-2:])
print(tuple2[::-1])
print(tuple2[::-1])
print(3 in tuple2)
print(3 not in tuple2)
print(5 in tuple2)
del tuple2
# print(tuple2)

