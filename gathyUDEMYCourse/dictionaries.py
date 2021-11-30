
# DICTIONARIES
# THEY ARE MUTABLE

dict1 = {}
print(dict1)
print(type(dict1))
dict1 = {"Vendor": "Cisco", "Model": "2600", "IOS": "12.4", "Ports": "4"}
d1 = {1: "First element", 2: "Second element"}

print(dict1)
print(dict1["IOS"])
print(dict1["Vendor"])
dict1["RAM"] = "128"
print(dict1)
dict1["IOS"] = "12.3"
print(dict1)
del dict1["Ports"]
print(dict1)
print(len(dict1))
print("IOS" in dict1)
print("IOS2" in dict1)
print("IOS2" not in dict1)
print(dict1.keys())
print(dict1.values())
print(dict1.items())

# CONVERSIONS BETWEEN DATA TYPES

num = 2
f = 2.5
num2 = str(num)
print(type(num2))
f2 = str(f)
print(type(f2))
str1 = "5"
int1 = int(str1)
print(type(int1))
f3 = float(str1)
print(type(f3))
f4 = float(num)
print(type(f4))

tup1 = (1,2,3)
list1 = list(tup1)
print(type(list1))
list1 = [1, 2, 3]
tup2 = tuple(list1)
print(type(tup2))

num = 10
num_bin = bin(num)
print(num_bin)

num_hex = hex(num)
print(num_hex)

bin_to_num = int(num_bin, 2)
print(bin_to_num)

hex_to_num = int(num_hex, 16)
print(hex_to_num)

