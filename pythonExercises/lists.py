# LISTS

li = [1,2,3,4,5]
li2 = ['a', 'b', 'c']
li3 = [1,2,'a', True]

# DATA STRUCTURE

amazon_cart = ['notebooks',
               'sunglasses',
               'toys',
               'grapes'
               ]
print(amazon_cart[0])
print(amazon_cart[1])

# LIST SLICING \
print(amazon_cart) #gets all in the list
print(amazon_cart[0::2]) # will get all from start to end but skip every second one

# LISTS ARE MUTABLE so can change one if we like. lets say we dont want notebooks in the cart anymore so we change it to something else like a laptop. its this simple
amazon_cart[0] = 'laptop'
print(amazon_cart) # now when ran we see it says laptop instead of notebooks


print(amazon_cart[0:3]) # with list slicing we are making a new copy of the original list. and only carrying over whatever parts we want. see how orginal list will not be changed after slicing it
print(amazon_cart)

#so we could save the sliced original list as a new variable if we wanted too

new_cart = amazon_cart[0:3]
new_cart[0] = 'gum'
print(new_cart)


