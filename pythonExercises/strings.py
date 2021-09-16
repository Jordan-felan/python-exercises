#strings
print(type('hi, hello there'))
print(type("hi, hello there"))

username = 'supercoder'
password = 'supersecret'
long_string = '''
WOW
0 0
___
'''
print(long_string) #multi line strings ^^^

first_name = 'Jordan'
last_name = 'Felan'
full_name = first_name + ' ' + last_name
print(full_name)

#string concatenation or adding strings together how we did above
print('Jordan ' + 'Felan')


#cant add a string and and int without type conversion
#Type Conversion
print(type(str(100))) #this will be a class of string
print(type(int(str(100)))) #this will be a class of integer


#Escape Sequence is basically adding a \ slash before the apostrophe or double quote
weather = "It's \"kind of\" sunny"
print(weather)

# \t adds a tab spacing right after
# \n adds a line break right after


# Formatted Strings
#to do so we just add an f at the beginning

name = 'Jordan'
age = 26

print(f'hi {name}. You are {age} years old') #way to go because it looks much cleaner

#old way to do it that still works in python 3
print('hi {}. You are {} years old'.format(name, age))

#also can switch the order of the variables with its index number. always starts at 0 then 1 then 2 etc..
print('hi {1}. You are {0} years old'.format(name, age))

#can also set new variables to fill the brackets
print('hi {new_name}. You are {age} years old'.format(new_name='sally', age=100))


# String Indexes
#strings are stored in memory as an ordered sequence of characters
#just like indexes in JS or Java

selfish = '01234567'
#          01234567

print(selfish[0]) #grabbing whatever is at the index of 0
print(selfish[7]) #grabbing whatver is at the index of 7
print(selfish) #is grabbing everything that is index 0-7

#can also do this [start:stop] which basically grabs everything from starting point to the end point. Will grab everything from the start to the last index before the stop
print(selfish[0:2]) #which should return index 0 and 1 which happens to be 0 and 1

print(selfish[0:7]) #will return all index from the start 0 to whatever is right before the index 7 which is 0123456

print(selfish[0:8]) #this will grab every index because there is actually 8 characters total so this will return 01234567

#there also is a stepover
# [start:stop:stepover]
print(selfish[0:8:1]) #default is a stepover of 1, will return the entire string or whatever is between the start and stop point

#but if we add a 2 in the stepover point it will stepover 2 indexs so this next one should return 0246 because it will skip over 2 indexes every time
print(selfish[0:8:2])

#can also not include a stop and just a start. so example below will start at index 1 and print everything after since there is no stop
print(selfish[1:])

#and can be done vice versa. so if i dont put a start and only an end it will start at the very beginning and stop at whatver you set the stop index to be. so example below will start at the first index which is zero and stop at index 5
print(selfish[:5])

# in using the negative sign before an index tells it to start at the end of the string so -1 should return the last index of the string
print(selfish[-1])

# so -2 would do the second from last index of the string and so on and so on

#should return second to last index of the string
print(selfish[-2])

#should return the third from last index of the string
print(selfish[-3])

#also if we add a negative stepover lets say one of -1 it will reverse the string
print(selfish[::-1]) #very usefull to reverse the order

print(selfish[::-2]) #will reverse the string and skip 2



# Immutability which means things that cannot be changed

# selfish = '01234567'
# #          01234567

selfish = 100
print(selfish)

# but cannot change a single index for example this will throw and error selfish[0] = 8. This is something we cannot do. You have to create something new either by concatting or reassigning selfish as a whole





