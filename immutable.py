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

my_string = "the variable is {}".format(var) #the format method prints whatever is assigned to var

my_string = "the variable is {} and {:.2f}".format(var, var2) #the format method prints whatever is assigned to var, the decimal places of var2 is specified by ':2f'

#the newest method of formatting strings
my_string = f"the variable is {var} and {var2*2}" #the f-string method prints whatever is assigned to var and var2


#Tuple are unordered, contains different data types, immutable, and does not allow duplicates
my_tuple = tuple((1, "name", True)) #created a tuple
my_tuple = (1, "name", True) #creates a tuple
