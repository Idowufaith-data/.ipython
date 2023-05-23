#Lists are mutable, ordered, contains different data types and allows duplicates
my_list = list([1, "name", True]) #this command also creates a list
my_list = [ 1, "name", True] #the output will be given in this ordered; i.e lists are ordered

my_list[1] = "faith" #lists are mutable; name has been permanently changed to faith in the list

my_list.append("idowu") #lists are mutable; idowu has been added to the list

my_list.remove(1) #will remove the number 1 from the list

my_list.insert(2, False) #inserts False at index number 2

my_list.reverse() #reverses the items in the lists and prints them from the last to the first

#my_list.sort() #sorts the items in ascending order it alters the list

my_list.pop() #returns the last item from a list and also removes that item from the list

my_list.clear() #clears all the items in the list
list1 = [1,2,3,4,5]
list2 =['bananas', 'apples', 'mangoes', 'oranges']

# Combining two lists together
list1.extend(list2)
print(list1)

# Adding constants to a list
list2.append('cherry')
print(list2)


# To find the length of a list
print(len(list2))

# Inserting a constant into a list
list2.insert(1, 'cherry') # 1 in this case is the index number where 'cherry' will be placed
print(list2)

# Removing a constant from a list
list2.remove('bananas')
print(list2)

# To clear everything in a list
list2.clear()
print(list2)

# To get the index number of a constant in a list
print(list2.index('mangoes'))

# To figure out the number of times a value appears in a list
print(list2.count('mangoes'))

# To print a list in ascending order
list1.sort()
print(list1)

# To print a list in reverse 
list1.reverse()
print(list1)

# To duplicate a list
list3 = list2.copy()
print(list3)

# To delete the last value from a list and print everything else
list2.pop()
print(list2)

# To delete a specific value using their index number 
list2.pop(1) #This will remove the value at index no 1 
print(list2)

# To delete a specific value using their index number
del list2[0] #This will delete the value at index no 0
print(list2)

# To delete a list
del list1

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

#Dictionary are mutable, ordered, are created in the as keys:values, allows duplicates
