''' Abstract Classes & Methods'''

''' An abstract class can be considered as a blue print for other classes.
Abstract class :- a class which contains one or more abstract methods is known as abstract class
Abstract method :- a method that has declaration but doesn't have implementation is known as abstract method.

when we use an abstract class?
while we are designing large functional units we use an abstract class.
when we want to provide a common Interface for different implementations of a component, we use abstract class,
like API's(Application Program Common Interface) etc..
'''

''' by default python didn't support abstraction.
but we have a best module to implement abstraction called "ABC" module. 
we need to import and inherite that module to implement abstraction in python
'''

from abc import ABC, abstractmethod

''' abstract classes can have both abstract methods and concrete(normal) methods. but abstract methods must be implemented in subclass '''

class Animal(ABC): # inheriting ABC to make abstract class
    @abstractmethod # by defining @abstratmethod annotation, below method becomes abstract method otherwise normal(concrete) method.
    def move(self):
        pass
    def eat(self): #concrete method
        print('eating')
class Human(Animal):
    def move(self):
        super().eat()  # accessing concrete method of abstract class using super() keyword
        print('walk and run')
class Snake(Animal):
    def move(self):
        print('crawl')

r = Human()
r.move()
s = Snake()
s.move()

