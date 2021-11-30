
# SETS

# list4 = [1,2,3,4,5,2,3]
# print(set(list4))
# set1 = set([11, 12, 13, 14, 15, 15, 15, 11])
# print(set1)
# print(type(set1))
# set2 = {11, 12, 13, 14, 15, 15, 15, 11}
# print(set2)
# print(type(set2))
# print(len(set2))
# print(11 in set2)
# print(10 in set2)
# print(10 not in set2)
# set2.add(16)
# print(set2)
# set2.remove(11)
# print(set2)
# set2.add(16)
# print(set2)

# SET METHODS
set1 = {1, 2, 3, 4}
set2 = {3, 5, 8}
print(set1.intersection(set2))
print(set2.intersection(set1))
print(set1.difference(set2))
print(set2.difference(set1))
print(set1.union(set2))
set1.pop()
print(set1)
set1.clear()
print(set1)

# FROZEN SETS are immutable sets
list1 = {1, 2, 3, 4}
list2 = {3, 4, 7}

fs1 = frozenset(list1)
fs2 = frozenset(list2)
print(type(fs1))
# fs1.add(10)
# fs1.remove(1) NONE OF THESE WILL WORK
# fs1.pop()
# fs1.clear()

print(fs1.intersection(fs2))
print(fs1.difference(fs2))
print(fs1.union(fs2))

