class Dog():
    def __init__(self, name):
        self.name = name
        
    def bark(self):
        print("I am a dog and my name is", self.name)
        print("bark")

d = Dog("Bingo")
d.bark()