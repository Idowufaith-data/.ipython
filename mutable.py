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

#Dictionary are mutable, ordered, are created in the as keys:values, allows duplicates
