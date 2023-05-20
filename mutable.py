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

#Dictionary are mutable, ordered, are created in the as keys:values, allows duplicates
