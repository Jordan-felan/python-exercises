
# LISTS
# list1 = []
# print(type(list1))

list1 = ["Cisco", "Juniper", "Avaya", 10, 10.5, -11]

# print(len(list1))
# print(list1[0])
# print(list1[1])
# print(list1[-1])
# print(list1[-2])
# print(list1[2])
# list1[2] = "HP"
# print(list1)

# LIST METHODS

list2 = [-11, 2, 12]
# print(min(list2))
# print(max(list2))
#
# list3 =["a", "b", "c"]
# print(min(list3))
# print(max(list3))

# CANT USE MIN MAX ON LIST WITH STRINGS AND NUMBERS IN IT

list1.append(100)
# print(list1)
# del list1[4]
# print(list1)
# list1.pop(0)
# print(list1)
# list1.remove("Juniper")
# print(list1)
# list1.insert(2, "Nortel")
# print(list1)
# list1.extend(list2)
# print(list1)
# print(list1.index(-11))
# print(list1.count(10))
list2.append(1)
list2.append(25)
list2.append(500)
# print(list2)
# list2.sort()
# print(list2)
# list2.reverse()
# print(list2)
# sorted(list2)
# print(list2)
# sorted(list2, reverse = False)
# print(list2 * 3)

# LIST SLICING
list3 = [1, 2, 3, "a", "b", "c"]
print(list3)
print(list3[0:3])
print(list3[:3])
print(list3[2:5])
print(list3[2:])
print(list3[:])
print(list3[-1])
print(list3[-2])
print(list3[-4:-1])
print(list3[-3:])
print(list3[:-3])
print(list3[::2])
print(list3[::-1])

