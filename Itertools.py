#Itertools module: is a collection of tools for handling iterators. Simply put, iterators are data types that can be used in a 'for' loop.
# The most common iterator is a list but itertools offers some advanced tools.
# These are: product, permutations, combinations, accumulate, groupby, and infinite iterators

from itertools import product
a = [1,2]
b = [3,4]
prod = product(a,b)
print(list(prod)) #This will print the products in this order [(1,3), (1,4), (2,3), (2,4)]
prod = product(a,b, repeat=2)
print(list(prod)) #prints the values in a 

