#Variables can be named anything as long as we set it equal to something
#Variable rules:
#1 always snake_case
#2 start with a lowercase or an underscore
#3 contain letters, numbers, and underscores. p.s variables that start with an underscore are considered private variables
#4 case sensitive
#5 dont overwrite key words. which means words that are already used in python for example print()
#6 name things really well with your variables

# user_iq = 190

#reassigning variable

# user_age = user_iq/4

#or

# a = user_age
#
#
# print(user_age)
# print(a)

#can also set multiple variables at once
# a,b,c = 1,2,3
# print(a)
# print(b)
# print(c)

#constants. Set them all in caps to let developers know it should not be changed. It still can be changed tho if wanted
# PI = 3.14



#dunder variables start with doubles underscores. we should not create variables like this and only use the built in ones


#Expressions and Statements

iq = 100
user_age = (iq/5) #<-- this is the expression and a statement is an entire line of code that performs an action

#augmented assignment operator
some_value = 5
some_value += 2  #this will also be like some_value = 5 + 2 can be used with addition +=, subtraction -= and multiplication *=

print(some_value)