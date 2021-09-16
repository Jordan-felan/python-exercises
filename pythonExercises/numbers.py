#Fundamental Number Datatypes

#int = integer example: 0, 1, 2, 3
#float = decimal point numbers Example: 1.5, 0.5
#complex

# #ints and floats are stored as binary
# print(bin(5)) #gets binary representation
# print(int('0b101', 2)) #returns as number to the base of 2. Should return 5

# print(type(2+4))
# print(type(2-4))
# print(type(2*4))
# print(type(2/4)) #type is float because is 0.5

# print(type(20+1.1))
# print(20+1.1)

# the ** double multiplication signs means power of. So example below is 2 to the power of 2 which is 4
# print(2 ** 2)
# print(2**3) #2 to the power of 3 which should be 8

# #using // double division signs makes it rounds it down to the nearest integer for example 2//4 will give you 0 where as 5//4 would give you 1
# print(2//4)
# print(5//4)

#using the % modulo sign is used to represent the remainder of the division for example 5 % 4 would give you a 1. because that is the remainder of 5 divided by 4
# print(5 % 4)
# print(6 % 3)

#Math Functions can always google for full list of Math Functions. There are so many! can google them by "python mathmatical functions"

# #ROUND
# print(round(3.1))
# print(round(3.9))
#
# #ABS absolute value of the arguement
# print(abs(-20))

#OPERATOR PRECENDENCE is just like PEMDAS
# () Parentheses
# ** Power Of or Exponent
# * / Multiplication and division
# + - Addition and Subtraction

# print(20 - 3 * 4)

#EXERCISE FOR Operator Precedence
#Guess what the output will be for each code snippet
print((5 + 4) * 10 / 2) #45

print(((5 + 4) * 10) / 2) #45

print((5 + 4) * (10 / 2)) #45

print(5 + (4 * 10) / 2) #25

print(5 + 4 * 10 // 2) #25

#Complex Data Type
# complex()