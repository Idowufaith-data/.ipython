#Strings are immutable, ordered, contains numbers or character in single, double or triple quotes, text representatio
my_string = "Hello World" #strings are created with single, double or triple quotes

my_string2 = 'I\'m a programmer' #the escape operator(\) can be used to print single quotes

my_string3 = """ Hello
 World""" #triple quotes is also used for multi line strings

char = my_string[0] #prints the character at index 0 i.e H

#my_string[0] = 'h' #this command will cause an error because strings are immutable i.e cannot be changed

substring = my_string[1:5] #This process is called 'slicing' and it'll print characters in index 1 to 4

substring = my_string[::2] #prints every second character and the first character i.e 0,2,4,6 e.t.c

substring[::-1] #reverses the string

greeting = "Hello"
name = "Faith"
sentence = greeting + " " + name #strings can be concatenated or joined together

#strings can be iterated i.e
#for x in greeting: 

#you can check if there's a character or a substring in the string using
#if 'ello' in greeting:
    #print('yes')
#else:
    #print('no')

#methods in strings

my_string = my_string.strip() #removes whitespaces from the string, does not change the original string unless it is assigned to it because strings are immutable
my_string = my_string.upper() #changes the characters in the string to upper case alphabets
my_string = my_string.lower() #changes the characters in the string to lowere case alphabets
my_string = my_string.startswith('H') #confirms if the strings starts with the character H
#my_string = my_string.endswith('d')#confirms if the strings ends with the character d
#my_string = my_string.find('d')#returns the first index where it finds the character d
#my_string = my_string.count('o') #returns the count of a particular character in a string
#my_string = my_string.replace('World', "Universe") #replaces World with Universe and it doesn't change the original string

#converting a string to a list
my_string = 'how are you doing'
my_list = my_string.split() #splits every word according to the whitespaces and puts them in a list

new_string = ', '.join(my_list) #converts the list back to a string, whatever is specified in between the new string('') is used to print the output

#formatting strings
var = "Faith"
var2 = 3.22245
my_string = "the variable is %s" % var #%s acts a placeholder for whatever is assigned to var

#Sets are immutable, unordered, allow different data types, do not allow duplicates, cannot be subscripted because they are unordered, only fellow immutables can be added to a set, True and 1 or 0 and false are duplicates in aset because true means 1 and 0 means false, an empty set cannot br created with {} but set(), methods do not permanently modify the original set
myset = {1, 2, 3, 4, 5} #creates a set
myset = set([1, 2, 3, 4, 5]) or set("Hello") #creates a set

myset = {1, 2, 3, 4, 5, 6, 1, 3} #1 and 3 will be printed just once because sets do not allow duplicates

myset = set() #creates an empty set

#sets are mutable therefore values can be added into the empty set above using the .add method
myset.add(1)
myset.add(2)
myset.add(3)

myset.remove(3) #removes the item 3 from our set, gives an error if it cannot find the item
myset.discard(3) #removes the item 3 from our set, doesnt give an error if it doesn't find the item
myset.pop() #returns the arbitrary value of the set and also prints it
myset.clear() #removes all items from the set

#iterating through our set can be done using
for i in myset:
    print(i) #will iterate through the elements and prints it

#to check if an element is in our set we can use the if statement
if 1 in myset:
    print('yes')
else:
    print('no')

#unions, intersections, differences and symmetric_difference will not alter the original set
odds = {1, 3, 5, 7, 9, 11, 13,}
evens = {0, 2, 4, 6, 8}
primes = {2, 3, 5, 7}

u = odds.union(evens)  #unions combines elements from both sets without duplication
i =  odds.intersection(primes) #intersection will only print elements that are found in both sets

#to calculate the difference of two sets
diff = odds.difference(primes) #difference will return all elements from the first set that are not in the second set

sym_diff = odds.symmetric_difference(primes) #symmetric difference returns all elements that are not present in both sets 

#to alter the original sets
odds.update(primes) #updates odds with the values from primes without duplicates
odds.intersection_update(primes) #updates the set by keeping only the elements found in both sets
odds.difference_update(evens) #updates the first set and prints all elements in the first set that are not in the second set
odds.symmetric_difference_update(evens) #updates the first set by keeping only elements that are not in both sets

#subset, superset and disjoint methods
print(evens.issubset(odds)) #subset is true if all the elements of the first set are also in the second set
print(evens.issuperset(odds)) #superset is true if the first set contains *all the numbers* in the second set
print(evens.isdisjoint(odds)) #disjoint is true if both sets do not have the same elements

#copying sets
odd = odds #assigns the values in odds to odd, alters the original set(odds)

odd = odds.copy() #assigns the values in odds to odd, without altering the original set(odds)
odd = set(odds) #assigns the values in odds to odd, without altering the original set(odds)

#frozen set is a collection of data types like set but it is immutable; unions, intersections e.t.c will work 
a = frozenset([1, 2, 3, 4])
print(a)

a.add(2) #will give an error because frozen sets are immutable
a.remove(1) #will give an error because frozen sets are immutable

my_string = "the variable is {}".format(var) #the format method prints whatever is assigned to var

my_string = "the variable is {} and {:.2f}".format(var, var2) #the format method prints whatever is assigned to var, the decimal places of var2 is specified by ':2f'

#the newest method of formatting strings
my_string = f"the variable is {var} and {var2*2}" #the f-string method prints whatever is assigned to var and var2


#Tuple are unordered, contains different data types, immutable, and does not allow duplicates
my_tuple = tuple((1, "name", True)) #created a tuple
my_tuple = (1, "name", True) #creates a tuple
# Tuples are used to store multiple items in a variable. Tuples are immutable; they allow 
# the repetiton of the same values, they allow various data types. Tuples are useful when one is
# working on co-ordinates, values you dont want to change e.t.c

# Construct a tuple
three_numbers = tuple((1, True, 'home'))

three_numbers = (1,2,3,'home',1, True)
strings = ('land', 'home', 'earth')
boo = (True, False, True)
print(three_numbers)

# To find the number of values in a tuple
print(len(three_numbers))

# To find the type of a tuple
print(type(three_numbers))

# To find the data type of a specific tuple
print(type(three_numbers[0]))
