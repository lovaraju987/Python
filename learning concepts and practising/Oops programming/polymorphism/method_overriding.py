''' Method Overriding '''

''' Method Overriding :
overriding super class methods by defining same methods in subclass is known as method overriding.
'''

class A:
    def display(self):
        print('this method is class of A')

class B(A):
    def display(self): # overriding display method of class A
        print('this method is class of B')

obj = B()
obj.display()