# A class is like a blueprint for creating objects. An object has properties and methods(functions) associated with it. Almost everything in Python is an object

#Create Class
class User:
    #constructor
    def __init__(self, name, age, email, status):
        self.name = name
        self.age = age
        self.email = email
        self.status = status

    def greetings(self):
        print(f'Name:{self.name}, Age:{self.age}, Email:{self.email}, Status:{self.status}')

# Extends classes
class Customer(User):
    def __init__(self, name, age, email, status, balance):
        self.balance = balance


#Initiazing Object

brad = User('Brad', 34, 'test@test.com','Active')

janet = Customer()

brad.greetings()


