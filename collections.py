import collections
#Collections module implements special container data types and provides alternatives with some additional functionality compared to the other built-in containers. 
#Types:Counter, namedtuple, OrderedDict, defaultdict, and deque

#1. Counter: is an container that stores the elements as dictionary keys and their counts as dictionary values
#from collections import Counter
a = "aaaabbbbbbbbcccccc"
#my_counter = Counter(a)
#print(my_counter)
#print(my_counter.values()) #To view the values alone
#print(my_counter.keys()) #To view the keys alone
#print(my_counter.most_common(1)) #To view the most common element, just the first one
#print(my_counter.most_common(1)[0][0]) #To view the most common element, the first tuple and the first key of thr most common tuple
#print(list(my_counter.elements())) # will print all the elements one by one arranged into a list e.g ['a', 'a', 'a', 'a' e.t.c]

#namedtuple: similar to a struct
from collections import namedtuple
Point = namedtuple('Point', 'x,y') #This will create a class called Point with fields x and y7
pt = Point(1,-4) #Creating the class Point with the field values 1 and -4 for x and y respectively
print(pt)
print(pt.x, pt.y) #This will print the values assigned to x and to y

#OrderedDict: is just like a regular dictionary but it remembers the order in which the elements are placed
from collections import OrderedDict
ordered_dict = OrderedDict()
ordered_dict['a'] = 1
ordered_dict['b'] = 2
ordered_dict['c'] = 3
ordered_dict['d'] = 4
print(ordered_dict) #This will print a dictionary where the values are placed according to our order of placement

#defaultdict: must have a default value if the key has not been set yet
from collections import defaultdict
d = defaultdict(int)
d['a'] = 1
d['b'] = 2
print(d) #Will print a dictionary which has a default class/type which is an int (<class 'int'>, {'a':1, 'b':2})
print(d['a']) #Will print the the value which is 1 in this case
print(d['c']) # When a key that does not exist is put in, it'll give the default value of an int(type that was specified) which is 0

#deque: is a double ended queue and it can be used to add or remove elements from both ends
from collections import deque
d = deque()
d.append(1)
d.append(2)
print(d) #This will print elements arranged into a list
 
d.appendleft(3) #This will append 3 to the left side/beginning of the list
d.extend([4,5,6]) #This will add the elements 4,5, and 6 to the end of our list/right side
d.extendleft([4,5,6]) #This will add the elements 4,5, and 6 to the begining of our list/left side in this order [6, 5, 4]
d.rotate(1) #This will rotate all elements to the right according to the specified number of places which is 1 in this case
d.rotate(-1) #This will rotate all elements to the left according to the specified number of places which is 1 in this case
d.pop() #This will remove the last element in the list
d.popleft() #This will return and remove the first element on the left side
d.clear() #Removes all elements