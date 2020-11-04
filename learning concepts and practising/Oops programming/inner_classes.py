''' Inner classes or nested class'''

class Student:
    def __init__(self,name,age,study,branch):
        self.name = name
        self.age = age
        self.study = study
        self.branch = branch

    def show(self):
        print(self.name,self.age,self.study,self.branch)

    class Laptop:
        def __init__(self,brand,price,ram,processor):
            self.brand = brand
            self.price = price
            self.ram = ram
            self.processor = processor
        
        def show(self):
            print(self.brand,self.price,self.ram,self.processor)

s1 = Student('raju',19,'engineer','CME') #creating object for outer class
s1.show()
lp = s1.Laptop('Asus',44000,'8gb','Ryzen5') #creating object for inner class. we can also directly create object for inner class using outer class name
lp.show()

''' 
inner classer are two types :
They are : 1) Multiple Inner classes - creating multiple inner classes in outer class is know as multiple innner class
           2) Multilevel Inner clalsses  - creating creating another inner class in inner class. it is hierarchy. this type of classes is multivel inner calsses
           '''
print()
print()







#this program shows how to create object for inner class in outer class and send arguments
class Color: 
	
    def __init__(self,name,name1,code): 
        self.name = name
        self.lg = self.Lightgreen(name1,code) #creating object for inner class in outer class. and we can initialize arguments directly without taking arguments from outer class like "Lightgreen('lightgreen','saf34r')" 
	
    def show(self): 
        print("Name:", self.name) 
	
    class Lightgreen: 
        def __init__(self,name,code): 
            self.name = name
            self.code = code
        
        def display(self): 
            print("Name:", self.name) 
            print("Code:", self.code) 

outer = Color('Green','Lightgreen','sfso422') 

outer.show()

l = outer.lg #accessinig inner class object created in outer class

l.display()