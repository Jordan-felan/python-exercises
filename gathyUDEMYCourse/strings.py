# my_string = 'this is my first string'
# my_string = '''this
# is
# my
# first
# string'''

# my_string = '''this
# is\
# my\
# first\
# string'''
# print(my_string)
#
# string1 = "Cisco Router"
# print(string1[0])
# print(string1[2])
# print(string1[5])
# print(string1[-1])
# print(string1[-4])
# print(len(string1))



# STRING METHODS
# a = "Cisco Switch"
# print(a.index("i"))
# print(a.count("i"))
# print(a.find("sco"))
# print(a.lower())
# print(a.upper())
# print(a.startswith("C"))
# print(a.endswith("h"))
# b = "   Cisco Switch   "
# print(b.strip())
# c = "$$$Cisco Switch$$$"
# print(c.strip("$"))
# print(b.replace(" ", ""))
# d = "Cisco, Juniper, HP, Avaya, Nortel"
# print(d.split(","))
#
# print("_".join(a))

# STRINGS OPERATORS AND FORMATTING

# x = "Cisco"
# y = " Switch"
#
# print(x + y)
#
# print("o" in x)
# print("b" in x)
# print("b" not in x)
#
# format = "Cisco model: %s, %d WAN slots, IOS %f" % ("2600XM", 2, 12.4)
# print(format)
#
# format2 = "Cisco model: {0}, {1} WAN slots, IOS {2}".format("2600XM", 2, 12.4)
# print(format2)
#
# model = "2600XM"
# slots = 4
# ios = 12.3
# format3 = f"Cisco model: {model.lower()}, {slots * 2} WAN slots, IOS {ios}"
# print(format3)

# STRING SLICES
string1 = "O E2 10.110.8.9 [160/5] via 10.119.254.6, 0:01:00, Ethernet2"
print(string1[5:15])
print(string1[5:])
print(string1[:15])
print(string1[:])
print(string1[-1])
print(string1[-2])
print(string1[-9:-1])
print(string1[-5:])
print(string1[:-5])
print(string1[::2])
print(string1[::-1])

# SLICING USING A STEP
mystring = "0123456789"
print(mystring[0])
print(mystring[1])
print(mystring[9])
print(mystring[::2])
print(mystring[1::2])
print(mystring[1:7:2])




