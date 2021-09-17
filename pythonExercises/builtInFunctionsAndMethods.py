# Built in Functions and Methods

# so far learned about
# str()
# int()
# print()
# type()
# abs()

# Link to more built in methods and functions
# https://docs.python.org/3/library/functions.html

# String built in functions

# len() which is short for length. Also count doesnt start at 0 it starts at 1
print(len('helllooooo'))

greet = 'helllooooo'
print(greet[0:len(greet)])

# built in String methods
 # LINK TO MORE STRING METHODS
# https://www.w3schools.com/python/python_ref_string.asp
#automatic tools to use on strings

quote = 'to be or not to be'

print(quote.upper())    #Everything gets capitalized

print(quote.capitalize())    #Capitalizes the first letter of the string

print((quote.lower()))  #Lower cases everything

print(quote.find('be')) # tells me if the word be is in the string and if it is will tell you what index it starts on. So example here would start at index three

print(quote.replace('be', 'me')) # replaces all occurances of the word specified to be replaced. In this example the word "be" will be replaced with the word "me" at every place it appears in the specified string

#so after using the replace method up above this what will happen if i just print the string again? will it be changed because of the replace method i used above?

print(quote)  # It will return the original string because strings are immutable, that means they cannot be changed. We can overwrite them but not change them. We either create them or destroy them. So when we use the replace method above we are creating a new string not altering the original and since we are not assigning the string to anything as soon as it is printed it is removed from memory

# But if i do something like this we are creating a whole new string and storing it as the quote2 variable
quote2 = quote.replace('be', 'me')
print(quote2)
print(quote) # quote will always stay the same because it is immutable


