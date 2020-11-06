''' Method Overloading '''

''' Method Overloading:
usig same methods multiple times with different arguments is known as method overloading.
but in python this way is not working. to acheive method overloading in python we can use 'None' keyword to argument values. 
let us see how it works..
'''

class Opertations:
    def sum(self,a=None,b=None,c=None,d=None): # by using this None keyword we can call this functions with arguments are without arguments based on what we need
        
        if a is not None and b is not None and c is not None and d is not None:
            return a+b+c+d
        elif a is not None and b is not None and c is not None:
            return a+b+c
        elif a is not None and b is not None:
            return a+b
        elif a is not None:
            return a
        else:
            return None
        

o = Opertations()
print(o.sum())
print(o.sum(10))
print(o.sum(10,20))
print(o.sum(10,20,30))
print(o.sum(10,20,30,40))