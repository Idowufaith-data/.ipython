# Object Oriented Programming is simply the creation of user defined objects that are of user specified types. For example: when we assign a constant to the variable and the check for the type of the variable, the answer will be in the format 'class "datatype"'. Class here means that 'the constant is an object of that data type'

#Now let's take a more pratical exaample:
x = 50
print(type(x)) #When you run this you'll get <class 'int'>, this means that variable x which is assigned to the constant 50 is an object of the class int.

#The objects above are created from built-in functions like the assignment operator (=) but creating a user defined class requires more that'll be considered in this article.

#Classes: Classes are also the blueprint or prototype for creating objects because python is an object oriented programming language i.e because python sees functions, strings, classes, types e.t.c as objects.

#The class creates a user-defined data structure, which holds it's own data members and functions which can be accessed and used by creating an instance/object of that class. We can simply say that classes provide a means of bundling data into one place where they can function together.

#Classes consist of :
# Attributes
# Method
# Special methods

# Basic syntax of a class
class ClassName:
    def methodname(self): # This is called a function outside a class but it is called a 'method' once it's in a class
        print("Anything you'll like to print")

c = ClassName() #This process is similar to the assignment process in built-in classes but it is called 'object instantiation' in this type of class. An object (c in this case) will be created.

c.methodname() #Calling of the method and this is done by attaching (.) followed by the method's name to the object
#Note: The 'self' parameter will be explained later in this article

#Objects(also called Instance): An object is an instance of a class; as we stated earlier that a class is a blueprint for creating objects, objects are just the copy of the classes with actual values. An object consists of:
# State: It is represented by the attributes of an object. It also reflects the properties of an object
# Behaviour: It is represented by the methods of an object. It also reflects the response of an object to other objects.
# Identity: It gives a unique name to the object and enables one object interact with other objects.

#Example:
class Dog():
    def __init__(self, name):#name is the object or instance's attribute
        self.name = name
        
    def bark(self): #bark is the method's identity
        print("I am a dog and my name is", self.name)
        print("bark") #the def method and the statements in it are the object's behavior

d = Dog("Bingo")
d.bark()

#Class Attribute vs Object Attribute

#class attribute are variables defined in the class and it can be shared by all objects of the class while object/instance attribute are properties unique to an instance/object of a class,
class Dog():
    class_attribute1 = "mammal" # class attribute 

    def dog(self, name): #name here is an object/instance attribute 
        self.name = name
        print("My name is", self.name)
        print("I'm a", self.class_attribute1)

d = Dog()
d.dog("Bingo")

#Special Methods 

# __init__() method: The __init__ method is similar to constructors in C++ and Java. They are used to initialize the object's state. They also contain a collection of statements or instructions that are executed at the time of the object creation. It arun as soon as an object of a class is instantiated. This method is useful to do any initialization one wants to do with objects.
#Example:
class Person:
    def __init__(self, name):
        self.name = name
    def greeting(self):
        print("Hello, my name is", self.name)

p = Person('Faith')
p.greeting()

#Note: That the name was passsed while instantiating the object, this is because the __init__ method is also executed at the point where the object is created.

#__str__() method: This method is used to define how a class object should be represented as a string. It is used to give objects human-readable textual representation, which is helpful for logging, debugging or showing users object information.

#Example:
class String:
    def __init__(self, name, company):
        self.name = name
        self.company = company
    def __str__(self):
        return f"my name is {self.name} and I work at {self.company}"
s = String("Faith", "Computer")
print(s)