''' Types of Methods in object Oriented'''

''' There are three types of methods in python oops. 
they are 1) Instance mehtods
         2) class methods
         3) static methods
'''

class Student:
    college = 'gitam' #class attributes
    def __init__(self,m1,m2,m3):  #constructors
        self.m1 = m1  #instance attributes
        self.m2 = m2
        self.m3 = m3

    def avg(self):  #instance methods - related to objects
        return (self.m1+self.m2+self.m3)/3
    
    def info(self):  #instance methods can access class attributes
        self.college = 'andhra'
        return self.college

    @classmethod     #class methods - it uses @classmethod symbol and requires 'cls' argument. we can call class methods using both objects and class name
    def info2(cls):
        cls.college = 'tamil'
        return cls.college
    
    @staticmethod  #static methods - it uses @staticmethod symbol and didn't requires any agument. we can call static methods also using both objects and calss name
    def info3():
        Student.college = 'chennai'
        return Student.college


s1 = Student(10,20,30)

print(s1.avg())  #calling instance methods using objects

print(s1.info()) #calling instance methods using objects by accessiing class attributes

print(s1.info2(),Student.info2())#calling class methods using both object and class name

print(s1.info3(),Student.info3()) #calling static methods using both object and class name

''' difference between class methods and static methods :
class methods - this method can access and modify the class state. it know the state of the class
static methods - this method can not access and mofify the calss state. because it did not know the state of the class. static methods uses for some utility tasks
'''




