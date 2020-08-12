#1 Basic Structure
class Dog():
    def __init__(self,mybreed, name, spots):    #Constructor of the class - created automatically
        
        #ATTRIBUTES
        #We take in the argument
        # Assign it using self.atribute_name
        self.breed = mybreed        #  self - instance of the object 
        self.name = name
        #spots boolean
        self.spots = spots
my_dog= Dog(mybreed='Golden Retriever', name='Scooby', spots=False)       #mybreed just an argument
print(my_dog.breed)                     #breed is the actual attribute
print(my_dog.name)
print(my_dog.spots)

#2 Methods and Functions
class Dog():

    #Class Object Attribute
    #same for any instance of the class
    species = 'mammal'
    def __init__(self,mybreed, name, spots):    #Constructor of the class - created automatically
        
        #ATTRIBUTES
        #We take in the argument
        # Assign it using self.atribute_name
        self.breed = mybreed        #  self - instance of the object 
        self.name = name
        #spots boolean
        self.spots = spots

    #Operations/Actions ----> Methods
    def bark(self, number):     #no need for self.number as we are going to provide it in function call - not connected to an instance
        print(f"WOOF!! My name is {self.name}, I am a {self.breed} and I am {number} years old")      #self to refer that instance of that name  

my_dog= Dog('Lab','Rocky',True)       #mybreed just an argument
print(my_dog.breed)                     #breed is the actual attribute
print(my_dog.name)
print(my_dog.spots)
print(my_dog.species)
my_dog.bark(4)


#3 contd.
class Circle():

    #Class Object Attribute
    pi = 3.14
    def __init__(self,radius=1):
        self.radius = radius
    #Method
    def circumference(self):
        return self.radius * self.pi * 2     #need to do self.pi to access Class Object Attribute
mycircle = Circle(30)
print(mycircle.circumference())
        
#4 Inheritance 

#Base class
class Animal():

    def __init__(self):
        print("Animal created")
    def who_am_i(self):
        print("I am an animal")
    def eat(self):
        print("I am eating")

#Derived class
class Dog(Animal):
    def __init__(self):
        Animal.__init__(self)        #call Animal init fn
        print("Dog Created")
    def who_am_i(self):
        print("I am a dog")
    def bark(self):
        print("WOOF!!")

myanimal = Animal()    #Animal Attributes
myanimal.eat()
myanimal.who_am_i()

#derived class attributes of the base class - can call attributes of the base class
mydog = Dog()
mydog.eat()
mydog.who_am_i()        #can overwrite base method
myanimal.who_am_i()     #doesnt reflect in base method
mydog.bark()            #Added new method

#5 Polymorphism
class Dog():
    def __init__(self,name):
        self.name = name
    def speak(self):
        return self.name + " Says woof!"

class Cat():
    def __init__(self,name):
        self.name = name
    def speak(self):
        return self.name + " Says meow!"

niko = Dog("Niko")
felix = Cat("Felix")
print(niko.speak())     #Same method name but different instances of the class - different classes 
print(felix.speak())    #can call the same function

#6 Abstract classes
#no need to be instantiated - no need to create an instance

class Animal():
    def __init__(self,name):
        self.name = name
    def speak(self):
        raise NotImplementedError("Subclass must implement this abstract method")
        #speak to not do anything in base class
        #expected to create a subclass(inherit base class) and overwrite this method to call
        #no need to create instance of the class

class Dog(Animal):
    #no need for init
    def speak(self):
        return self.name + " says WOOF!!"

class Cat(Animal):
    #no need for init
    def speak(self):
        return self.name + " says MEOWW!!"

rocky = Dog('Rocky')
isis = Cat('ISIS')

rocky.speak()
isis.speak()

#7 Special Functions
class Book():
    def __init__(self,title,author,pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f"{self.title} by {self.author}"
    def __len__(self):
        return self.pages
    def __del__(self):
        print("A book object has been deleted")

b = Book('Python Rocks', 'Pronnoy',200)
print(b)
print(len(b))
del b

#8 Homework
    #1.
class Line:
    
    def __init__(self,coor1,coor2):
        self.coor1 = coor1
        self.coor2 = coor2
    
    def distance(self):
        return ((self.coor2[0]-self.coor1[0])**2 + (self.coor2[1]-self.coor1[1])**2)**0.5
    
    def slope(self):
        return (self.coor2[1]-self.coor1[1])/(self.coor2[0]-self.coor1[0])

coordinate1 = (3,2)
coordinate2 = (8,10)
print(coordinate1[0],coordinate1[1],coordinate2[0],coordinate2[1])
li = Line(coordinate1,coordinate2)
print(li.distance())
print(li.slope())


    #2.
class Cylinder:
    
    pi = 3.14
    def __init__(self,height=1,radius=1):
        self.height = height
        self.radius = radius
        
    def volume(self):
        return self.pi*(self.radius)**2*(self.height)
    
    def surface_area(self):
        return 2*self.pi*(self.radius)*(self.height)

c = Cylinder(2,3)
print(c.volume())
print(c.surface_area())

#9 Challenge
class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    def deposit(self,amount):
        self.balance+= amount
        print(f"{amount} dollars deposited")
    def withdraw(self,amount):
        if amount>self.balance:
            print("Funds Unavailable, Try Again!")
        else:
            print(f"Withdrawal of {amount} dollars was accepted")
            self.balance-=amount
    def __str__(self):
        return f"Account Owner:    {self.owner} \nAccount Balance:  {self.balance}"

acct1 = Account('Pronnoy',500)
print(acct1)
acct1.deposit(50)
print(acct1.balance)
acct1.withdraw(20)
print(acct1.balance)
acct1.withdraw(900)